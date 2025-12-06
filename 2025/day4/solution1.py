import sys

sum_paper = 0


def add_to_result(data, verbose=False, message: str = None):
    global sum_paper
    verbose and message and print(message)
    sum_paper += data


def calculer_nb_same_ligne(ligne, coord):
    nb = 0
    if coord != 0 and ligne[coord - 1] == "@":
        nb += 1
    if coord != (len(ligne) - 1) and ligne[coord + 1] == "@":
        nb += 1
    return nb


def calculer_nb_different_ligne(ligne, coord):
    nb = 0
    if coord != 0 and ligne[coord - 1] == "@":
        nb += 1
    if ligne[coord] == "@":
        nb += 1
    if coord != (len(ligne) - 1) and ligne[coord + 1] == "@":
        nb += 1

    return nb


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        verbose = False
        verbose_vict = False
        verbose_repre = False
        first_line = True
        ligne_prec = ""
        ligne_traite = ""
        ligne_suiv = ""
        liste_repre = list()
        for ligne in f:
            verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")

            if ligne_prec == "":
                ligne_prec = ligne
                verbose and print(f"ligne_prec OK")
                continue

            if ligne_traite == "":
                ligne_traite = ligne
                verbose and print(f"ligne_traite OK")
                continue

            ligne_suiv = ligne

            if first_line:
                first_line = False
                ligne_repre = ""
                verbose and print(f"first ligne !")
                for x in range(0, len(ligne_prec)):
                    elt = ligne_prec[x]
                    verbose and print(f"{elt=}")
                    if elt == "@":
                        nb = 0
                        nb += calculer_nb_same_ligne(ligne_prec, x)
                        nb += calculer_nb_different_ligne(ligne_traite, x)
                        if nb < 4:
                            add_to_result(data=1, verbose=verbose_vict, message=f"Match first ligne !")
                            ligne_repre += "x"
                        else:
                            ligne_repre += "@"
                    else:
                        ligne_repre += elt
                verbose_repre and print(f"{ligne_repre=}")
                liste_repre.append(ligne_repre)
            ligne_repre = ""

            verbose and print("-- ")
            ligne_repre = ""
            for x in range(0, len(ligne_traite)):
                elt = ligne_traite[x]
                if elt == "@":
                    nb = 0
                    nb += calculer_nb_different_ligne(ligne_prec, x)
                    nb += calculer_nb_same_ligne(ligne_traite, x)
                    nb += calculer_nb_different_ligne(ligne_suiv, x)
                    if nb < 4:
                        add_to_result(data=1, verbose=verbose_vict, message=f"Match !")
                        ligne_repre += "x"
                    else:
                        ligne_repre += "@"
                else:
                    ligne_repre += elt
            verbose_repre and print(f"{ligne_repre=}")
            liste_repre.append(ligne_repre)
            ligne_prec = ligne_traite
            ligne_traite = ligne_suiv

        verbose and print(f"last ligne !")
        ligne_repre = ""
        for x in range(0, len(ligne_traite)):
            elt = ligne_traite[x]
            if elt == "@":
                nb = 0
                nb += calculer_nb_different_ligne(ligne_prec, x)
                nb += calculer_nb_same_ligne(ligne_traite, x)
                if nb < 4:
                    add_to_result(data=1, verbose=verbose_vict, message=f"Match last ligne !")
                    ligne_repre += "x"
                else:
                    ligne_repre += "@"
            else:
                ligne_repre += elt
        verbose_repre and print(f"{ligne_repre=}")
        liste_repre.append(ligne_repre)

        return sum_paper


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
