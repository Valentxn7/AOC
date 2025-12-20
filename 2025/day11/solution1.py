import sys

nb_appel = 0
OBJECTIF = "out"
DEPART = "you"
memo = dict()
noeud_dict = dict()


def plonger(provenance: str, verbose: bool = False) -> int | float:
    verbose and print(f"plonger({provenance=})")
    global nb_appel
    nb_appel += 1
    if provenance in memo.keys():
        verbose and print(f"memo({provenance=})")
        return memo[provenance]
    # verbose and print("plonger...")
    # verbose and print(f"{inital_toogle_p=}, {change_toogle_p=}, {index=}, {objectif=}")

    if provenance == OBJECTIF:
        verbose and print("find !")
        return 1

    sum_chemin = 0
    for one_destinataire in noeud_dict[provenance]:
        sum_chemin += plonger(one_destinataire, verbose)
    memo[provenance] = sum_chemin

    return sum_chemin

def solve(input_file):
    with (open(input_file, "r", encoding="utf-8") as f):
        verbose = False
        verbose_vict = False
        noeud_depart = None
        for ligne in f:
            verbose and print(f"Ligne non traitée : {ligne=}")
            ligne_decoupee: list[str] = ligne.split(':')
            provenance = ligne_decoupee[0]
            destinataire = tuple(ligne_decoupee[1].strip().split(' '))
            noeud = (provenance,) + destinataire
            verbose and print(f"Ligne traitée : {provenance=}{destinataire=}{noeud=}")
            assert provenance == noeud[0]

            if provenance == DEPART:
                noeud_depart = provenance
            noeud_dict[provenance] = destinataire

        # bruteforce
        best_nb_change: float = float("inf")
        nb_change: int = 0
        result = None

        result = plonger(noeud_depart, verbose=verbose)
        return result

    verbose_vict and print(f"{nb_appel=}")


if __name__ == "__main__":
    result = solve(sys.argv[1]) # "2025_day11_data"
    print(result)