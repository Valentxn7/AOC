import sys

sum_joltage = 0


def add_to_result(data, verbose=False, message: str = None):
    global sum_joltage
    verbose and message and print(message)
    sum_joltage += data


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        verbose = False
        verbose_vict = False
        for ligne in f:
            if ligne == "":  # derniere ligne vide
                continue

            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")

            ligne = list(ligne)
            max1 = max(ligne[:-1])
            max1_index = ligne.index(max1)
            max2 = max(ligne[max1_index + 1:])
            concatenation = max1 + max2
            verbose and print(f"{max1=}, {max2=} {concatenation=}")

            add_to_result(int(concatenation))
        return sum_joltage


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
