import sys


class Tile:
    def __init__(self, tile_char: str):
        self.char: str = tile_char
        self.energized: bool = False
        self.duplicated: bool = False

        if tile_char == '.':
            self.type = "void"
        elif tile_char == '^':
            self.type = "Splitter"
        elif tile_char == 'S':
            self.type = "Start"
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
            if elt.type == 'Start':
                ligne_affichage = ligne_affichage + 'S'
            elif elt.energized:
                ligne_affichage = ligne_affichage + '|'
            else:
                ligne_affichage = ligne_affichage + '.'
        print(ligne_affichage)


def count_energized(game: list[list[Tile]]) -> int:
    nb_energized = 0
    for ligne_game in game:
        for elt in ligne_game:
            if elt.energized:
                nb_energized = nb_energized + 1
    return nb_energized


start: tuple[int, int] | None = None
game: list[list[Tile]] = []
verbose: bool = False


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        nbLigne = -1
        for ligne in f:
            if ligne == "":  # derniere ligne vide
                continue
            nbLigne = nbLigne + 1
            # print(f"Ligne entière : {ligne=}")
            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")

            game.append([])
            for char in ligne:
                objectType = Tile(char)
                game[nbLigne].append(objectType)

                if char == 'S':
                    start = (len(game[nbLigne]) - 1, 0)
                    verbose and print(f"Start trouvé: {start=}")

        rayons: list[Rayon] = [Rayon(start[0], start[1], 'b')]
        max_x = len(game[0]) - 1
        max_y = len(game) - 1

        verbose and print(f"{max_x=}, {max_y=}")
        while rayons:  # tant qu'il y a des rayons pas encore échoué
            for rayon in rayons:
                rayon.se_deplacer()
                verbose and print(f"Rayon déplacé: {rayon=}")
                if rayon.is_dead(max_x, max_y):
                    verbose and print(f"Rayon mort!: {rayon=}")
                    rayons.remove(rayon)
                    continue
                case = game[rayon.y][rayon.x]

                match case.type:
                    case "void":
                        verbose and print(f"Rayon rencontre du vide...")
                        pass
                    case "Splitter":
                        if case.duplicated:
                            verbose and print(f" ^ déjà dupliqué, on évite la boucle!")
                            rayons.remove(rayon)
                            continue
                        case.duplicated = True
                        verbose and print(f"Rayon rencontre un ^ !")
                        verbose and print(f"Multiclonage !")
                        rayon1 = Rayon(rayon.x + 1, rayon.y, 'b')  # celui à droite
                        rayon2 = Rayon(rayon.x - 1, rayon.y, 'b')  # celui à gauche
                        verbose and print(f"Deux nouveau rayon: {rayon1=}{rayon2=}")
                        rayons.append(rayon1)
                        rayons.append(rayon2)
                        rayons.remove(rayon)
                        case.energize()
                    case '_':
                        raise ValueError(f"Erreur type Tile {case.type=}")

    verbose and afficher_jeu(game=game)
    verbose and afficher_energized(game=game)
    return count_energized(game=game)


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
