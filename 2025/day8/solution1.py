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

    iteration = -1
    for distance, box_choisie, meilleur_pair in all_distance:
        iteration += 1
        if iteration == 1000:
            break

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

                verbose and print(f"DEBUG {list_junction=}")
                verbose and print(f"## merge junction {meilleur_pair.junction=} with {box_choisie.junction=}")
                list_junction.remove(meilleur_pair.junction)
                box_choisie.junction.merge(meilleur_pair.junction)
                verbose and print(f"## after merge {box_choisie.junction=}")
                verbose and print(f"DEBUG {list_junction=}")
        else:
            new_junction = junction()
            verbose and print(f"## creating junction {new_junction=}")
            new_junction.add_box(box_choisie)
            new_junction.add_box(meilleur_pair)
            box_choisie.junction = new_junction
            meilleur_pair.junction = new_junction
            list_junction.append(new_junction)
            verbose and print(f"## after creating {new_junction=}")

    # trouver les plus grosse junction
    total = 1
    verbose and print(f"{list_junction=}")
    for sum_i in range(0, 3):
        verbose and print(f"add best junction n{sum_i}")
        max_taille = 0
        meilleur_junction: junction | None = None
        for one_junction in list_junction:
            if one_junction.taille() > max_taille:
                max_taille = one_junction.taille()
                meilleur_junction = one_junction
        total *= max_taille
        verbose and print(f"meilleur junction : {meilleur_junction=}")
        list_junction.remove(meilleur_junction)

    return total


if __name__ == "__main__":
    result = solve(sys.argv[1])  #
    print(result)
