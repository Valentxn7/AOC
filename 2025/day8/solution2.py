import sys
from box_class import box
from junction_class import junction

verbose: bool = False


def solve(input_file):
    # on upload tout le ficher
    list_box: list[box] = list()
    list_junction: list[junction] = list()
    with open(input_file, 'r') as f:
        nbLigne = -1
        for ligne in f:
            if ligne == "":  # derniere ligne vide
                continue
            nbLigne = nbLigne + 1
            # print(f"Ligne entière : {ligne=}")
            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")
            x, y, z = ligne.split(",")
            verbose and print(f"Ligne splited : {x=}, {y=}, {z=}")
            new_box = box(int(x), int(y), int(z))
            list_box.append(new_box)

    all_distance: list[tuple[float, box, box]] = list()
    for i in range(0, len(list_box)):
        box_choisie = list_box[i]
        verbose and print(f"- {box_choisie=}")
        for y in range(i, len(list_box)):
            if y == i: continue
            box_comparee = list_box[y]
            distance = box_choisie.distance(box_comparee)
            all_distance.append((distance, box_choisie, box_comparee))
            verbose and print(f"-- {box_comparee=}, {distance=}")

    all_distance.sort(key=lambda tup: tup[0])
    verbose and print(f"all_distance={all_distance}")

    initalized = False
    box_1: box | None = None
    box_2: box | None = None
    for distance, box_choisie, meilleur_pair in all_distance:
        verbose and print(f"* {distance=} {box_choisie=} {meilleur_pair=}")
        if len(list_junction) == 1 and len(list_junction[0].box_list) == len(list_box):
            verbose and print(f"finie")
            return box_1.x * box_2.x
        box_1, box_2 = box_choisie, meilleur_pair
        if box_choisie.junction or meilleur_pair.junction:
            if not meilleur_pair.junction:  # box1 en a une mais pas box2, on ajoute box2 dans Junct1
                verbose and print(f"## add to existing junction {box_choisie.junction=}")
                box_choisie.junction.add_box(meilleur_pair)
                meilleur_pair.junction = box_choisie.junction
                verbose and print(f"## after add {box_choisie.junction=}")
            elif not box_choisie.junction:  # box2 en a une mais pas box1, on ajoute box1 dans Junct2
                verbose and print(f"## add to existing junction {meilleur_pair.junction=}")
                meilleur_pair.junction.add_box(box_choisie)
                box_choisie.junction = meilleur_pair.junction
                verbose and print(f"## after add {meilleur_pair.junction=}")
            else:  # les deux ont une junction: on merge
                if box_choisie.junction == meilleur_pair.junction:
                    verbose and print(f"## same junction")
                    continue

                # verbose and print(f"DEBUG {list_junction=}")
                verbose and print(f"## merge junction {meilleur_pair.junction=} with {box_choisie.junction=}")
                list_junction.remove(meilleur_pair.junction)
                box_choisie.junction.merge(meilleur_pair.junction)
                verbose and print(f"## after merge {box_choisie.junction=}")
                # verbose and print(f"DEBUG {list_junction=}")
        else:
            new_junction = junction()
            verbose and print(f"## creating junction {new_junction=}")
            new_junction.add_box(box_choisie)
            new_junction.add_box(meilleur_pair)
            box_choisie.junction = new_junction
            meilleur_pair.junction = new_junction
            list_junction.append(new_junction)
            verbose and print(f"## after creating {new_junction=}")


if __name__ == "__main__":
    result = solve(sys.argv[1])  # "2025_day8_data"
    print(result)
