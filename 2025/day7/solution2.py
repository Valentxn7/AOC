import sys
from functools import cache  # memoize integre a pyhton


def solve(input_file):
    verbose = False
    game: list[list[str]] = list()
    start: tuple[int, int] | None = None

    # on upload tout le ficher
    with open(input_file, 'r') as f:
        nbLigne = -1
        for ligne in f:
            if ligne == "":  # derniere ligne vide
                continue
            nbLigne = nbLigne + 1
            # verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")

            game.append([])
            for char in ligne:
                game[nbLigne].append(char)

                if char == 'S':
                    start = (len(game[nbLigne]) - 1, 0)

    max_y = len(game) - 1
    verbose and print(f"{max_y=}")
    verbose and print(f"{game=}")
    verbose and print(f"{start=}")

    @cache
    def deplacer(x, y):
        verbose and print(f"{x=} {y=}")
        if y >= max_y:
            verbose and print("dcd")
            return 1

        if game[y][x] == "^":
            verbose and print("split")
            return deplacer(x - 1, y) + deplacer(x + 1, y)
        else:
            verbose and print(".")
            return deplacer(x, y + 1)

    return deplacer(start[0], start[1])


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
