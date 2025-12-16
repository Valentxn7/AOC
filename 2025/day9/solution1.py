import sys

verbose: bool = False


def distance(point1, point2):
    return ((max(point1[0], point2[0]) - min(point1[0], point2[0])) + 1) * (
            (max(point1[1], point2[1]) - min(point1[1], point2[1])) + 1)


def solve(input_file):
    # on upload tout le ficher
    max_x: int = 0
    max_y: int = 0
    with open(input_file, 'r') as f:
        nbLigne = -1
        coord_red: list[tuple[int, int]] = list()
        for ligne in f:
            if ligne == "":  # derniere ligne vide
                continue
            nbLigne = nbLigne + 1
            # print(f"Ligne entière : {ligne=}")
            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")
            x, y = ligne.split(",")
            x = int(x)
            y = int(y)
            if x > max_x: max_x = x
            if y > max_y: max_y = y
            verbose and print(f"Ligne splited : {x=}, {y=}")
            coord_red.append((x, y))

        verbose and print(f"{max_x=} {max_y=}")
        verbose and print(f"{coord_red=}")

        coord_red.sort(key=lambda p: (p[1], p[0]))
        verbose and print(f"reversed {coord_red=}")
        dist_max = float("-inf")
        for i in range(0, len(coord_red) // 2):
            box_choisie = coord_red[i]
            verbose and print(f"- {box_choisie=}")
            for x in range(len(coord_red) // 2, len(coord_red)):
                box_comparee = coord_red[x]
                dist = distance(box_choisie, box_comparee)
                if dist > dist_max:
                    dist_max = dist
                verbose and print(f"-- {box_comparee=}, {dist=}")

    return dist_max


if __name__ == "__main__":
    result = solve(sys.argv[1])  # "2025_day9_data"
    print(result)
