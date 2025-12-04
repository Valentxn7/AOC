import sys

def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        ranges: list[tuple[int, int]] = []
        verbose = False
        count_mirror = 0
        for ligne in f:
            if ligne != "":  # derniere ligne vide
                # print(f"Ligne entière : {ligne=}")
                ligne = ligne.strip()
                verbose and print(f"Ligne traitée : {ligne=}")
                ranges_no_separated = ligne.split(",")
                for r in ranges_no_separated:
                    start, end = r.split("-")
                    ranges.append((int(start), int(end)))
        verbose and print(f"{ranges=}")

        # on recherche les doubles
        for r in ranges:
            verbose and print(f"Traitement de la range {r=}")
            verbose and print(f"{r[0]=}, {r[1]=}")
            for i in range(r[0], r[1] + 1):
                long = len(str(abs(i)))
                if long % 2 == 1:
                    continue
                    raise ValueError(f"Nombre de longueur impair détecté: {i=}")
                verbose and print(f"Traitement du nombre {i=}, {long=}")
                verbose and print(f"1er intervalle: [0:{long / 2}] 2eme intervalle: [{long / 2}:{long}]")
                if str(i)[0:int(long / 2)] == str(i)[int(long / 2):long]:
                    verbose and print(f"Nombre mirroir détecté, {i=}")
                    count_mirror += i
        return count_mirror

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
