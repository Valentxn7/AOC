import sys

nb_appel = 0
OBJECTIF = "out"
DEPART = "svr"
memo = dict()
noeud_dict = dict()


def plonger(provenance: str, is_dac: bool = False, is_fft: bool = False, verbose: bool = False) -> int | float:
    verbose and print(f"plonger({provenance=})")
    global nb_appel
    nb_appel += 1
    if (provenance, is_dac, is_fft) in memo.keys():
        verbose and print(f"memo({(provenance, is_dac, is_fft)=})")
        return memo[(provenance, is_dac, is_fft)]

    if provenance == "fft":
        is_fft = True

    if provenance == "dac":
        is_dac = True

    # verbose and print("plonger...")
    # verbose and print(f"{inital_toogle_p=}, {change_toogle_p=}, {index=}, {objectif=}")

    if provenance == OBJECTIF:
        verbose and print("find !")
        if is_dac and is_fft:
            verbose and print("all conditions !")
            return 1
        return 0

    sum_chemin = 0
    for one_destinataire in noeud_dict[provenance]:
        sum_chemin += plonger(one_destinataire, is_dac, is_fft, verbose)
    memo[(provenance, is_dac, is_fft)] = sum_chemin

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
    result = solve(sys.argv[1])
    #result = solve("2025_day11_data")
    print(result)
