from functools import cache

nb_appel = 0


@cache
def toogle_switch(inital_toogle_p: tuple[str, ...], change_toogle: tuple[int, ...]) -> tuple[str, ...]:
    inital_toogle: list[str] = list(inital_toogle_p)

    for index_to_change in change_toogle:
        if inital_toogle[index_to_change] == '#':
            inital_toogle[index_to_change] = '.'
        elif inital_toogle[index_to_change] == '.':
            inital_toogle[index_to_change] = '#'
        else:
            raise ValueError(f"Error toogle_switch: {inital_toogle=}, {change_toogle=}")
    return tuple(inital_toogle)

@cache
def plonger(inital_toogle_p: tuple[str, ...], change_toogle_p: tuple[tuple[int, ...], ...], actual_toogle: tuple[int, ...] | None,
            objectif: str, verbose: bool = False) -> int | float:
    global nb_appel
    inital_toogle: tuple[str, ...] = inital_toogle_p
    change_toogle: list[tuple[int, ...]] = list(change_toogle_p)
    nb_appel += 1
    verbose and print("plonger...")
    verbose and print(f"{inital_toogle=}, {change_toogle=}, {actual_toogle=}, {objectif=}")
    if not change_toogle:
        return float('inf')

    if actual_toogle:
        inital_toogle = toogle_switch(inital_toogle, tuple(actual_toogle))

        if "".join(inital_toogle) == objectif:
            verbose and print("find !")
            return 1

    result = list()
    for i in range(0, len(change_toogle)):
        temp_ch_toogle = change_toogle.copy()
        act_toogle = temp_ch_toogle[i]
        temp_ch_toogle.remove(act_toogle)
        act_toogle = tuple(act_toogle)
        if actual_toogle:
            plouf = 1 + plonger(inital_toogle, tuple(temp_ch_toogle), act_toogle, objectif, verbose)
            if plouf > 2:
                result.append(
                    plouf)  # si aucun ne l'a resout directement, on aller prend le minimum (le meilleur) de toutes les solutions
            else:
                verbose and print("OPTI: best result (1) directly find")
                return plouf
        else:
            result.append(plonger(inital_toogle, tuple(temp_ch_toogle), act_toogle, objectif, verbose))

    return min(result)


summary = 0
with open("2025_day10_data", "r", encoding="utf-8") as f:
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
        debug_btn_int = False
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

        all_boutons: tuple[tuple[int, ...], ...] = tuple(boutons_interessant) + tuple(boutons_linked)
        verbose and print(f"{all_boutons=}")

        # bruteforce
        TOOGLE_EMPTY: list[str] = ['.' for _ in range(len(switchs))]
        verbose and print(f"{TOOGLE_EMPTY=}")
        best_nb_change: int = 99999999999999
        nb_change: int = 0

        result = plonger(tuple(TOOGLE_EMPTY), all_boutons, None, switchs, verbose=False)
        print(f"{result=}")
        summary += result
        """
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
        """

print(f"{summary=}")
print(f"{nb_appel=}")
