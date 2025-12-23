import sys


def toogle_switch(inital_toogle_p: list[str], change_toogle: tuple[int]) -> list[str]:
    for index_to_change in change_toogle:
        if inital_toogle_p[index_to_change] == '#':
            inital_toogle_p[index_to_change] = '.'
        elif inital_toogle_p[index_to_change] == '.':
            inital_toogle_p[index_to_change] = '#'
        else:
            raise ValueError(f"Error toogle_switch: {inital_toogle_p=}, {change_toogle=}")
    return inital_toogle_p


def plongerV2_without_dic(actual_toogle_p: list[str], change_toogle_p: tuple[tuple[int], ...],
                          objectif: str, verbose: bool = False) -> int | float:
    verbose and print(f"plongerV2_without_dic({actual_toogle_p=}, {change_toogle_p=}, {objectif=})")
    # verbose and print(f"{inital_toogle_p=}, {change_toogle_p=}, {index=}, {objectif=}")

    if "".join(actual_toogle_p) == objectif:
        verbose and print("find !")
        return 0

    if len(change_toogle_p) == 0:  # aucune combinaison trouvée
        return float('inf')

    # on en prend pas
    no_take = None
    no_take = plongerV2_without_dic(actual_toogle_p.copy(), change_toogle_p[1:], objectif, verbose)
    if no_take <= 1:  # OPTI: évite de plongerV2_without_dic dans le second abre alors qu'on a déjà la meilleur solution
        # 1 car en dessous on fait déjà 1 + ... donc c'est déjà mieux
        # print(f"OPTI second arbre évité")
        return no_take

    # on prend
    take = None
    actual_toogle_toogled = toogle_switch(actual_toogle_p.copy(), change_toogle_p[0])
    take = 1 + plongerV2_without_dic(actual_toogle_toogled, change_toogle_p[1:], objectif, verbose)

    assert take is not None
    assert no_take is not None
    return min(no_take, take)


def solve(input_file):
    # on upload tout le ficher
    verbose = False
    verbose_vict = False
    summary = 0
    with open(input_file, "r", encoding="utf-8") as f:

        for ligne in f:
            verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.split()[:-1]  # les voltages ne nous intéresse pas

            for elt in range(1, len(ligne)):
                one_grp_button = ligne[elt]
                one_grp_button = one_grp_button.strip('(').strip(')')
                one_grp_button = one_grp_button.split(',')
                for ss_elt in range(0, len(one_grp_button)):
                    one_grp_button[ss_elt] = int(one_grp_button[ss_elt])
                ligne[elt] = one_grp_button

            verbose and print(f"Ligne traitée : {ligne=}")

            # on convertit en numéro les switch à avoir sur on
            switchs = ligne[0].strip('[').strip(']')
            verbose and print(f"{switchs=}")
            switchs_num: list[int] = list()
            for i in range(0, len(switchs)):
                if switchs[i] == '#':
                    switchs_num.append(i)
            verbose and print(f"{switchs_num=}")

            # on essaie de faire de l'élagage, on vire tout les boutons qui n'ont rien a faire
            # - les boutons qui ne contiennent pas nos nombres ET qui ne sont pas contenue dans ceux qui contiennent nos nombres
            all_boutons: tuple[tuple[int], ...] = tuple(
                map(tuple, ligne[1:]))  # DEBUG test si élégage bouton est en tord
            # print(f"all_boutons={all_boutons=}")
            verbose and print(f"{all_boutons=}")

            TOOGLE_EMPTY: list[str] = ['.' for _ in range(len(switchs))]
            result = plongerV2_without_dic(TOOGLE_EMPTY, all_boutons, switchs, verbose=verbose)

            verbose_vict and print(f"{result=}")
            summary += result

        return summary


if __name__ == "__main__":
    result = solve(sys.argv[1])  # "2025_day10_data"
    print(result)
