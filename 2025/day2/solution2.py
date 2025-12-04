import sys

count_mirror = 0


def add_to_result(data, verbose=False, message: str = None):
    global count_mirror
    verbose and message and print(message)
    count_mirror += data


def solve(input_file):
    # on upload tout le ficher
    global count_mirror
    with open(input_file, 'r') as f:
        ranges: list[tuple[int, int]] = []
        verbose = False
        verbose_vict = False
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
                if long < 2:
                    verbose and print(f"{i=} trop petit")
                    continue
                same_number = True
                double_number = False

                verbose and print(f"Traitement du nombre {i=}, {long=}")
                for j in range(0, long - 1):
                    # on test si tout le nombre est composé du même chiffre
                    verbose and same_number and print(f"test same_number {str(i)[j]=}, {str(i)[j + 1]=}")
                    if str(i)[j] != str(i)[j + 1]:
                        same_number = False
                        verbose and print(f"{same_number=}")
                        break

                if same_number:
                    add_to_result(i, verbose=verbose_vict, message=f"Same number for {i=} !")
                    continue

                if long < 4:
                    double_number = False
                    continue

                multiples_2_len = []

                for div_probable in range(2, int(long)):  # 2 car la répétition entière est déjà testé au dessus
                    if int(long) % div_probable == 0:
                        multiples_2_len.append(div_probable)

                verbose and print(f"{multiples_2_len=}")

                for div in multiples_2_len:
                    verbose and print('---')
                    partition = long // div
                    deb_ech = 0
                    fin_ech = 0 + partition
                    echantillon = str(i)[deb_ech:fin_ech]
                    verbose and print(
                        f"test double_number: {str(i)=} {echantillon=}, {partition=}, {deb_ech=}, {fin_ech=}")
                    nb_test_double_number = 0
                    for k in range(partition, long - 1, partition):
                        nb_test_double_number += 1
                        # On test si au moins une répétition de 2 chiffre existe
                        second_echantillon = str(i)[k:k + partition]
                        verbose and print(f"{nb_test_double_number=}")
                        verbose and print(
                            f"Comparaison entre l'échantillon et son suivant: {echantillon=}, {second_echantillon=}")
                        if second_echantillon == echantillon:
                            verbose and print(f"one match!")
                            verbose and print(f"test si fin de nombre {long=}, {k=} {partition=}, {k+partition=} ")
                            if (k + partition) >= long:  # si on a parcourut tout le nombre sans se bouffer le break
                                double_number = True
                                verbose_vict and print(f"Double number for {i=} !")
                                break
                        else:
                            break

                if same_number or double_number:
                    verbose_vict and same_number and print(f"Same number for {i=} !")
                    count_mirror += i
        return count_mirror


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
