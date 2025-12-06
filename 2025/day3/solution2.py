import sys

sum_joltage = 0


def add_to_result(data, verbose=False, message: str = None):
    global sum_joltage
    verbose and message and print(message)
    sum_joltage += data


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        verbose = True
        verbose_vict = True
        for ligne in f:
            if ligne == "":  # derniere ligne vide
                continue

            ligne = ligne.strip()
            verbose and print(f"Ligne traitée : {ligne=}")

            reste_a_prendre = 12
            ligne = list(ligne)
            concatenation = ""
            while reste_a_prendre > 0:
                choix = ligne[:-reste_a_prendre + 1] if reste_a_prendre > 1 else ligne
                max1 = max(choix)
                max1_index = ligne.index(max1)
                concatenation += max1
                verbose and print(f"{choix=} {max1=} {concatenation=} {reste_a_prendre=} ")
                reste_a_prendre -= 1
                ligne = ligne[max1_index + 1:]
            add_to_result(int(concatenation), verbose=verbose_vict, message=f" - fin: {concatenation=}")
        return sum_joltage


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
