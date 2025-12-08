import sys


verbose = False
verbose_vict = False
list_number: list[list[object]] = list()
max_length_list: list[int] = list()
orientation_list: list[str | None] = list()


def add_to_result(entire_data, added_data, verbose=False, message: str = None):
    verbose and message and print(message)
    entire_data += added_data


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        test_ingredient = False
        first_ligne_push = False
        for ligne in f:
            verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.split()
            verbose and print(f"Ligne traitée : {ligne=}")

            if not first_ligne_push:
                # initialiser la longueur max des colonnes
                len_inital_ligne = len(ligne)
                inital_ligne = [0 for inutile in range(len_inital_ligne)]
                max_length_list = inital_ligne  # list_number.append(inital_ligne)

                # initialiser le sens de collage des nombre: r or l
                inital_ligne = [None for inutile in range(len_inital_ligne)]
                orientation_list = inital_ligne  # list_number.append(inital_ligne)
                first_ligne_push = True

            for x in range(len_inital_ligne):
                verbose and print(f"{len(ligne[x])} > {max_length_list[x]} ?")
                if len(ligne[x]) > max_length_list[x]:  # connaitre la longueur max d'une colonne
                    max_length_list[x] = len(ligne[x])
            list_number.append(ligne)

            if ligne.__contains__("+") or ligne.__contains__("*"):
                verbose and print(f"Opérateur ! {list_number=}")
                break

    with open(input_file, 'r') as f:
        list_ligne: list[str] = list()

        for ligne in f:
            list_ligne.append(ligne)

        verbose and print(f"-- calcul de l'orientation")
        l1 = list_ligne[0]
        l2 = list_ligne[1]
        l3 = list_ligne[2]
        l4 = list_ligne[3]
        l_op = list_ligne[4]
        verbose and print(f"{l1=}, {l2=}, {l3=}, {l4=}, {l_op=}")
        nb_colonne = 0
        for x in range(0, len(l_op) - 1):
            if l_op[x] == "+" or l_op[x] == "*":
                verbose and print("opérateur trouvé ...")
                if l1[x] == " " or l2[x] == " " or l3[x] == " " or l4[x] == " ":
                    verbose and print("espace trouvé ...")
                    orientation_list[nb_colonne] = "r"
                else:
                    verbose and print("aucun espace trouvé ...")
                    orientation_list[nb_colonne] = "l"
                nb_colonne += 1
        verbose and print(f"{orientation_list=}")

    verbose and print(f"{max_length_list=}")
    sum_result = 0
    while len(list_number[0]) > 0:  # tant que on a pas finie (de droite à gauche)
        # pour chaque colonne
        result_memory = []
        number_memory = []
        vertical_number_memory = []
        boucle_max = max_length_list[len(list_number[0]) - 1]
        boucle_faite = -1
        operator = ""
        first_ligne_push = False

        verbose and print("---")
        for ligne in list_number:  # pour chaque ligne
            elt = ligne.pop()  # on prend le dernier chiffre en entier
            # verbose and print(f"{elt=}")

            if elt == "+":
                operator = "+"
            elif elt == "*":
                operator = "*"
            else:
                verbose and print(f"memorizing {elt}...")
                number_memory.append(elt)

        if operator == "":
            raise ValueError("Aucun opérateur n'a été lue")

        while boucle_faite < boucle_max - 1:  # tant qu'on a pas parcours chaque chiffre de la colonne
            boucle_faite += 1
            vertical_number = ""
            verbose and print(f"{number_memory=}, column_nb: {boucle_faite}")
            orientation = orientation_list[len(list_number[0])]  # pas de -1 car déjà pop
            assert orientation is not None  # toutes les colonnes doivent avoir une direction
            verbose and print(f"{orientation=}")
            for number in number_memory:  # pr chaque nombre de la colonne
                if orientation == "r":
                    verbose and print(f"{number=}, {len(number)=}, {boucle_max=}, {boucle_faite=}")
                    if len(number) > boucle_faite:  # vue qu'on parcours de gauche à droite, on ne doit pas dépasser le chiffre
                        # tmp_ind = boucle_faite if boucle_faite != 0 else 1
                        verbose and print(
                            f"vertical number found: {number}, chiffre retenue: {number[(-boucle_faite) - 1]}")
                        vertical_number += str(number[(-boucle_faite) - 1])
                else:
                    verbose and print(f"{number=}, {len(number)=}, {boucle_max=}, {boucle_faite=}, {boucle_faite=}")
                    if len(number) >= boucle_max - boucle_faite:
                        index = (boucle_max - boucle_faite) - 1
                        verbose and print(
                            f"vertical number found: {number}, chiffre retenue: {number[index]}")
                        vertical_number += str(number[index])
            assert vertical_number != ""  # on ne devrait pas avoir de conne vide si le boulot a bien été fait
            verbose and print(f"{vertical_number=}")
            vertical_number_memory.append((int(vertical_number)))

        if operator == "+":
            verbose and print(f"calculating addition of {vertical_number_memory}...")
            result = 0
            for number in vertical_number_memory:
                result += number
            verbose_vict and print(f"adding {result} to sum_result")
            sum_result += result
            verbose and print(f"{sum_result=}")
        elif operator == "*":
            verbose and print(f"calculating multiplication of {vertical_number_memory}...")
            result = 1
            for number in vertical_number_memory:
                result *= number
            verbose_vict and print(f"adding {result} to sum_result")
            sum_result += result
            verbose and print(f"{sum_result=}")
        else:
            raise ValueError(f"Invalid operator: {operator}")

    return sum_result


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
