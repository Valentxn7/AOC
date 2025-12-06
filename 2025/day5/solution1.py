import sys


def add_to_result(entire_data, added_data, verbose=False, message: str = None):
    verbose and message and print(message)
    entire_data += added_data


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        verbose = False
        verbose_vict = False
        test_ingredient = False
        list_fresh = set()  # pour éviter les doublons
        list_id_fresh_already_taken = set()
        somme_fresh = 0
        for ligne in f:
            # verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.strip()
            # verbose and print(f"Ligne traitée : {ligne=}")
            if ligne == '':
                test_ingredient = True
                verbose and print(f"{list_fresh}")
                continue

            if test_ingredient:
                for fresh_range in list_fresh:
                    if int(ligne) in fresh_range and int(ligne) not in list_id_fresh_already_taken:
                        somme_fresh += 1
                        list_id_fresh_already_taken.add(int(ligne))
                        verbose_vict and print(f"Ingrédient frais: {int(ligne)}")
                        # add_to_result(somme_fresh, 1, verbose=verbose_vict, message=f"Ingrédient frais: {id=}")
                continue

            ligne = ligne.split('-')
            min = int(ligne[0])
            max = int(ligne[1])
            list_fresh.add(range(min, max + 1))

        verbose and print(f"{list_fresh=}")
        return somme_fresh


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
