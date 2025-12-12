from functools import cache


def add_to_result(entire_data, added_data, verbose=False, message: str = None):
    verbose and message and print(message)
    entire_data += added_data


def toogle_switch(inital_toogle: list[str], change_toogle: list[int]) -> list[str]:
    for index_to_change in change_toogle:
        if inital_toogle[index_to_change] == '#':
            inital_toogle[index_to_change] = '.'
        elif inital_toogle[index_to_change] == '.':
            inital_toogle[index_to_change] = '#'
        else:
            raise ValueError(f"Error toogle_switch: {inital_toogle=}, {change_toogle=}")
    return inital_toogle


def plonger(inital_toogle_p: list[str], change_toogle_p: list[list[int]], objectif: str) -> int:
    inital_toogle: list[str] = inital_toogle_p.copy()
    change_toogle: list[list[int]] = change_toogle_p.copy()
    print("plonger...")
    print(f"{inital_toogle=}, {change_toogle=}, {objectif=}")
    if not change_toogle:
        return 0

    if "".join(inital_toogle) == objectif:
        return 1

    inital_toogle = toogle_switch(inital_toogle, change_toogle.pop())

    result = list()
    for i in range(0, len(change_toogle)):
        result.append(plonger(inital_toogle, change_toogle, objectif))

    return min(result)


with open("2025_day10_dataTEST", "r", encoding="utf-8") as f:
    verbose = True
    verbose_vict = True

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

        boutons_interessant = list()
        verbose and print(f" --- boutons_interessant")
        debug_btn_int = True
        for one_grp_button in ligne[1:]:
            debug_btn_int and print(f"{one_grp_button=}")
            for one_swt in one_grp_button:
                debug_btn_int and print(f"{one_swt=}")
                if one_swt in switchs_num:
                    boutons_interessant.append(one_grp_button)

        boutons_linked = list()
        verbose and print(f" --- boutons_linked")
        for one_grp_button in ligne[1:]:
            if one_grp_button in boutons_interessant:  # si déjà pris
                continue
            verbose and print(f"{one_grp_button=}")
            for one_swt in one_grp_button:
                verbose and print(f"{one_swt=}")
                for btn_int in boutons_interessant:
                    verbose and print(f"comparing to {btn_int=}")
                    if one_swt in btn_int:
                        if one_grp_button in boutons_linked:  # si déjà pris
                            continue
                        boutons_linked.append(one_grp_button)

        verbose and print(f"{boutons_interessant=}")
        verbose and print(f"{boutons_linked=}")

        all_boutons: list[list[int]] = boutons_interessant + boutons_linked
        verbose and print(f"{all_boutons=}")

        # bruteforce
        TOOGLE_EMPTY: list[str] = ['.' for _ in range(len(switchs))]
        verbose and print(f"{TOOGLE_EMPTY=}")
        best_nb_change: int = 99999999999999
        nb_change: int = 0

        print(f"{plonger(TOOGLE_EMPTY, all_boutons, switchs)=}")
        for first in range(0, len(all_boutons)):
            first = all_boutons[first]
            best_nb_change = 1
            toogle: list[str] = TOOGLE_EMPTY.copy()
            print(f"{first=} {toogle=}, {switchs=}")
            toogle = toogle_switch(inital_toogle=toogle, change_toogle=first)
            print(f"{first=} {toogle=}, {switchs=}")
            if toogle == switchs:
                print("find")
                if nb_change < best_nb_change:
                    best_nb_change = nb_change
            for second in range(0, len(all_boutons)):
                if first == second:
                    continue
                second = all_boutons[second]
                best_nb_change += 1
                toogle = toogle_switch(toogle, second)
                print(f"{second=} {toogle=}, {switchs=}")
                if toogle == switchs:
                    print("find")
                    if nb_change < best_nb_change:
                        best_nb_change = nb_change
        print(f"{best_nb_change=}")
