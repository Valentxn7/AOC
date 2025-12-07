import sys
import gc

all_verbose = False
verbose = all_verbose or False
verbose_vict = all_verbose or False

list_fresh: list[range] = list()  # pour éviter les doublons
somme_fresh = 0


def solve2():
    global somme_fresh, verbose, verbose_vict
    list_fresh.sort(key=lambda r: (r.start, r.stop))
    verbose and print(f"sorted: {list_fresh=}")
    merge: range | None = None
    for x in range(0, len(list_fresh) - 1):
        verbose and print("- - -")
        range1: range = list_fresh[x]
        range2: range = list_fresh[x + 1]
        verbose and print(f"{range1=}, {range2=}")
        verbose and print(f"{range1.start=}, {range1.stop=} -- {range2.start=}, {range2.stop=}")
        if merge:
            verbose and print("testing collision with merge...")
            if merge.stop >= range1.start:
                verbose and print("collision with merge.")
                assert min(merge.start, range1.start, range2.start) == merge.start
                range_deb = merge.start
                range_fin = max(merge.stop, range1.stop)
                merge = range(range_deb, range_fin)
                verbose and print(f"{merge=}")
                continue
            else:
                verbose and print("NO collision with merge, liberating merge...")
                range_long = len(merge) + 1
                verbose_vict and print(f"-- adding {range_long} by merge")
                somme_fresh += range_long
                merge = None
        if range1.stop >= range2.start:  # S'il y a une collision entre les 2 ensemble
            verbose and print("merge")
            if merge:
                verbose and print("Already a existing merge")
                assert min(merge.start, range1.start, range2.start) == merge.start
                range_deb = merge.start
                range_fin = max(merge.stop, range1.stop, range2.stop)
                merge = range(range_deb, range_fin)
            else:
                verbose and print("No existing merge")
                assert min(range1.start, range2.start) == range1.start
                range_deb = range1.start
                range_fin = max(range1.stop, range2.stop)
                merge = range(range_deb, range_fin)
            verbose and print(f"{merge=}")
        else:
            verbose and print("no merge")
            # on vide le buffer range si il a été remplit par des ensembles avec collision avant
            if merge:
                range_long = len(merge) + 1
                verbose_vict and print(f"-- adding {range_long} by merge")
                somme_fresh += range_long
                merge = None
            verbose and print(f"intervalle without collision: {range1}, {range1.start=}, {range1.stop=}")
            len_intervalle = (range1.stop - range1.start) + 1
            verbose_vict and print(f"-- adding {len_intervalle} by intervalle")
            somme_fresh += len_intervalle
    verbose and print(f"before final {somme_fresh=}")
    verbose and print("- - - Final - - -")
    x = len(list_fresh) - 1
    range1: range = list_fresh[x - 1]
    range2: range = list_fresh[x]
    verbose and print(f"{range1=}, {range2=}")
    verbose and print(f"{range1.start=}, {range1.stop=} -- {range2.start=}, {range2.stop=}")
    already_merge = False
    if merge:
        verbose and print("testing collision with merge...")
        if merge.stop >= range2.start:
            verbose and print("collision with merge.")
            assert min(merge.start, range1.start, range2.start) == merge.start
            range_deb = merge.start
            range_fin = max(merge.stop, range2.stop)
            merge = range(range_deb, range_fin)
            verbose and print(f"{merge=}")
            already_merge = True
        else:
            verbose and print("NO collision with merge, liberating merge...")
            range_long = len(merge) + 1
            verbose_vict and print(f"-- adding {range_long} by merge")
            somme_fresh += range_long
            merge = None
    if not already_merge and range2.stop >= range1.start:  # S'il y a une collision entre les 2 ensemble
        verbose and print("merge")
        if merge:
            verbose and print("Already a existing merge")
            assert min(merge.start, range1.start, range2.start) == merge.start
            range_deb = merge.start
            range_fin = max(merge.stop, range1.stop, range2.stop)
            merge = range(range_deb, range_fin)
        else:
            verbose and print("No existing merge")
            assert min(range1.start, range2.start) == range1.start
            range_deb = range1.start
            range_fin = max(range1.stop, range2.stop)
            merge = range(range_deb, range_fin)
        verbose and print(f"{merge=}")
    else:
        verbose and not already_merge and print("no merge")
        verbose and print(f"intervalle without collision: {range1}, {range1.start=}, {range1.stop=}")
        len_intervalle = (range1.stop - range1.start) + 1
        verbose_vict and print(f"-- adding {len_intervalle} by intervalle")
        somme_fresh += len_intervalle

    if merge:
        range_long = len(merge)
        verbose_vict and print(f"Final: adding {range_long} by merge")
        somme_fresh += range_long
        merge = None

    return somme_fresh


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        for ligne in f:
            # verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")
            if ligne == '':
                verbose and print(f"{list_fresh}")
                break

            ligne = ligne.split('-')
            ligne_min = int(ligne[0])
            ligne_max = int(ligne[1])
            list_fresh.append(range(ligne_min, ligne_max))

        f.close()
        del ligne, ligne_min, ligne_max, f
        gc.collect()

    return solve2()


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)