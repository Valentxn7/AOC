import sys


class Tile:
    def __init__(self, tile_char: str):
        self.char: str = tile_char  # caractère brut du puzzle (. / \ | -)
        self.energized: bool = False  # est-ce que la case est touchée par un rayon ?
        self.duplicated: bool = False

        # Déduction du type
        if tile_char == '.':
            self.type = "void"
        elif tile_char == '/':
            self.type = "rMirror"  # right mirror
        elif tile_char == '\\':
            self.type = "lMirror"  # left mirror
        elif tile_char == '|':
            self.type = "vSplit"  # vertical splitter
        elif tile_char == '-':
            self.type = "hSplit"  # horizontal splitter
        else:
            raise ValueError(f"Unknown tile: {tile_char}")

    def energize(self):
        self.energized = True

    def __repr__(self):
        return self.char


class Rayon:
    def __init__(self, x: int, y: int, d: str):
        self.x = x
        self.y = y
        self.direction = d

    def se_deplacer(self):
        match self.direction:
            case 'h':
                self.y = self.y - 1
            case 'r':
                self.x = self.x + 1
            case 'b':
                self.y = self.y + 1
            case 'l':
                self.x = self.x - 1

    def is_dead(self, max_x: int, max_y: int):
        return not ((0 <= self.x <= max_x) and (0 <= self.y <= max_y))

    def __repr__(self):
        return f"Rayon({self.x}, {self.y}, {self.direction})"


def afficher_jeu(game: list[list[Tile]]):
    for ligne_game in game:
        ligne_affichage = ''
        for elt in ligne_game:
            ligne_affichage = ligne_affichage + elt.__repr__()
        print(ligne_affichage)


def afficher_energized(game: list[list[Tile]]):
    for ligne_game in game:
        ligne_affichage = ''
        for elt in ligne_game:
            if elt.energized:
                ligne_affichage = ligne_affichage + '#'
            else:
                ligne_affichage = ligne_affichage + '.'
        print(ligne_affichage)


def reset_energize(game: list[list[Tile]]) -> None:
    for ligne_game in game:
        for elt in ligne_game:
            elt.energized = False


def reset_duplicates(game: list[list[Tile]]) -> None:
    for ligne_game in game:
        for elt in ligne_game:
            elt.duplicated = False


def reset_game(game: list[list[Tile]]) -> None:
    for ligne_game in game:
        for elt in ligne_game:
            elt.energized = False
            elt.duplicated = False


def count_energized(game: list[list[Tile]]) -> int:
    nb_energized = 0
    for ligne_game in game:
        for elt in ligne_game:
            if elt.energized:
                nb_energized = nb_energized + 1
    return nb_energized


def solve(input_file):
    verbose: bool = False
    game: list[list[Tile]] = []
    with open(input_file, 'r') as f:
        nbLigne = -1
        for ligne in f:
            if ligne != "":  # derniere ligne vide
                nbLigne = nbLigne + 1
                verbose and print(f"Ligne entière : {ligne=}")
                ligne = ligne[:-1]
                verbose and print(f"Ligne traitée : {ligne=}")

                game.append([])
                for char in ligne:
                    objectType = Tile(char)
                    game[nbLigne].append(objectType)

        verbose and afficher_jeu(game)

        max_x: int = len(game[0]) - 1
        max_y: int = len(game) - 1

        def resolve(rayons: list[Rayon]) -> int:
            verbose and print(f"{max_x=}, {max_y=}")
            while rayons:  # tant qu'il y a des rayons pas encore échoué
                for rayon in rayons:
                    rayon.se_deplacer()
                    verbose and print(f"Rayon déplacé: {rayon=}")
                    if rayon.is_dead(max_x, max_y):  # is dead ?
                        verbose and print(f"Rayon mort!: {rayon=}")
                        rayons.remove(rayon)
                        continue
                    case = game[rayon.y][rayon.x]
                    case.energize()

                    match case.type:
                        case "void":
                            verbose and print(f"Rayon rencontre du vide...")
                            continue
                        case "rMirror":
                            verbose and print(f"Rayon rencontre un / !")
                            match rayon.direction:
                                case "h":
                                    rayon.direction = "r"
                                case "r":
                                    rayon.direction = "h"
                                case "b":
                                    rayon.direction = "l"
                                case "l":
                                    rayon.direction = "b"
                        case "lMirror":
                            verbose and print(f"Rayon rencontre un \\ !")
                            match rayon.direction:
                                case "h":
                                    rayon.direction = "l"
                                case "r":
                                    rayon.direction = "b"
                                case "b":
                                    rayon.direction = "r"
                                case "l":
                                    rayon.direction = "h"
                        case "vSplit":
                            if case.duplicated:
                                verbose and print(f" | déjà dupliqué, on évite la boucle!")
                                rayons.remove(rayon)
                                continue
                            verbose and print(f"Rayon rencontre un | !")
                            match rayon.direction:
                                case "h" | "b":
                                    verbose and print(f"Bonne direction, je passe !")
                                case "l" | "r":  # DOIT POP LE NOTRE ET FAIRE SPAWN DEUX DOUBLE
                                    verbose and print(f"Multiclonage !")
                                    case.duplicated = True
                                    x = rayon.x
                                    y = rayon.y
                                    rayon1 = Rayon(x, y, 'h')  # celui qui monte
                                    rayon2 = Rayon(x, y, 'b')  # celui qui descend
                                    verbose and print(f"Deux nouveau rayon: {rayon1=}{rayon2=}")
                                    rayons.remove(rayon)
                                    rayons.append(rayon1)
                                    rayons.append(rayon2)
                        case "hSplit":
                            if case.duplicated:
                                verbose and print(f" - déjà dupliqué, on évite la boucle!")
                                rayons.remove(rayon)
                                continue
                            verbose and print(f"Rayon rencontre un - !")
                            match rayon.direction:
                                case "h" | "b":  # DOIT POP LE NOTRE ET FAIRE SPAWN DEUX DOUBLE
                                    verbose and print(f"Multiclonage !")
                                    case.duplicated = True
                                    x = rayon.x
                                    y = rayon.y
                                    rayon1 = Rayon(x, y, 'l')  # celui qui va a gauche
                                    rayon2 = Rayon(x, y, 'r')  # celui qui va a droite
                                    verbose and print(f"Deux nouveau rayon: {rayon1=}{rayon2=}")
                                    rayons.remove(rayon)
                                    rayons.append(rayon1)
                                    rayons.append(rayon2)
                                case "l" | "r":
                                    verbose and print(f"Bonne direction, je passe !")
                        case '_':
                            raise ValueError(f"Erreur type Tile {case.type=}")
            score2 = count_energized(game)  # 8112
            reset_game(game)
            reset_duplicates(game)
            return score2

        all_result: list[tuple[int, int, int]] = []

        verbose2 = False
        for y in range(max_y):
            # rayon débutant à gauche de haut en bas
            rayons: list[Rayon] = [Rayon(0 - 1, y, 'r')]  # -1 car se déplace dès le départ donc devient 0,0 direct
            result: tuple[int, int, int] = (0 - 1, y, resolve(rayons))
            verbose2 and print(f"x=-1 {y=} {result=}")
            all_result.append(result)

            # rayon débutant à droite de haut en bas
            rayons: list[Rayon] = [Rayon(max_x, y, 'l')]  # -1 car se déplace dès le départ donc devient 0,0 direct
            result: tuple[int, int, int] = (max_x, y, resolve(rayons))
            verbose2 and print(f"x={max_x} {y=} {result=}")
            all_result.append(result)

        for x in range(max_x):
            # rayon débutant en haut de gauche à droite
            rayons: list[Rayon] = [Rayon(x, 0 - 1, 'b')]  # -1 car se déplace dès le départ donc devient 0,0 direct
            result: tuple[int, int, int] = (x, 0 - 1, resolve(rayons))
            verbose2 and print(f"{x=} y=0 {result=}")
            all_result.append(result)

            # rayon débutant en haut de gauche à droite
            rayons: list[Rayon] = [Rayon(x, max_y + 1, 'h')]  # -1 car se déplace dès le départ donc devient 0,0 direct
            result: tuple[int, int, int] = (x, max_y + 1, resolve(rayons))
            verbose2 and print(f"{x=} y={max_y} {result=}")
            all_result.append(result)

        # rechercher le + grand score
        score_max = 0
        for score in all_result:
            if score[2] > score_max:
                score_max = score[2]
            if score[2] > 1000:
                verbose2 and print(f"gros score, {score=}")

        return score_max


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
