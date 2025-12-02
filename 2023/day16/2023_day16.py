class Tile:
    def __init__(self, tile_char: str):
        self.char: str = tile_char  # caractère brut du puzzle (. / \ | -)
        self.energized: bool = False  # est-ce que la case est touchée par un rayon ?

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
        return (not (0 <= self.x or self.x >= max_x)) or (not (0 <= self.y or self.y >= max_y))

    def __repr__(self):
        return f"Rayon({self.x}, {self.y}, {self.direction})"


rayons: list[Rayon] = [Rayon(0, 0, 'r')]
game: list[list[Tile]] = []
with open("2023_day16_dataTEST", "r", encoding="utf-8") as f:
    nbLigne = -1
    for ligne in f:
        if ligne != "":  # derniere ligne vide
            nbLigne = nbLigne + 1
            print(f"Ligne entière : {ligne=}")
            ligne = ligne[:-1]
            print(f"Ligne traitée : {ligne=}")

            game.append([])
            for char in ligne:
                objectType = Tile(char)
                game[nbLigne].append(objectType)

    max_x = len(game[0]) - 1
    max_y = len(game) - 1

    print(f"{max_x=}, {max_y=}")
    while rayons:  # tant qu'il y a des rayons pas encore échoué
        for rayon in rayons:
            rayon.se_deplacer()
            print(f"Rayon déplacé: {rayon=}")
            if rayon.is_dead(max_x, max_y):  # is dead ?
                print(f"Rayon mort!: {rayon=}")
                rayons.remove(rayon)
                continue
            case = game[rayon.y][rayon.x]

            match case.type:
                case "void":
                    print(f"Rayon rencontre du vide...")
                    pass
                case "rMirror":
                    print(f"Rayon rencontre un / !")
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
                    print(f"Rayon rencontre un \ !")
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
                    print(f"Rayon rencontre un | !")
                    match rayon.direction:
                        case "h" | "b":
                            pass
                        case "l" | "r":  # DOIT POP LE NOTRE ET FAIRE SPAWN DEUX DOUBLE
                            print(f"Multiclonage !")
                            rayon1 = Rayon(rayon.x, rayon.y, 'h')  # celui qui monte
                            rayon2 = Rayon(rayon.x, rayon.y, 'b')  # celui qui descend
                            print(f"Deux nouveau rayon: {rayon1=}{rayon2=}")
                            rayons.append(rayon1)
                            rayons.append(rayon2)
                            rayons.remove(rayon)
                case "hSplit":
                    print(f"Rayon rencontre un - !")
                    match rayon.direction:
                        case "h" | "b":  # DOIT POP LE NOTRE ET FAIRE SPAWN DEUX DOUBLE
                            print(f"Multiclonage !")
                            rayon1 = Rayon(rayon.x, rayon.y, 'l')  # celui qui va a gauche
                            rayon2 = Rayon(rayon.x, rayon.y, 'r')  # celui qui va a droite
                            print(f"Deux nouveau rayon: {rayon1=}{rayon2=}")
                            rayons.append(rayon1)
                            rayons.append(rayon2)
                            rayons.remove(rayon)
                        case "l" | "r":
                            pass
                case '_':
                    raise ValueError(f"Erreur type Tile {case.type=}")

    print(f"{game=}")
