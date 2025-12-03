import sys


def solve(input_file):
    # on upload tout le ficher
    with open(input_file, 'r') as f:
        actual_value = 50
        zero_count = 0
        verbose = False
        last_value_is_zero = False
        for ligne in f:
            if ligne != "":  # derniere ligne vide
                # print(f"Ligne entière : {ligne=}")
                ligne = ligne[:-1]
                # print(f"Ligne traitée : {ligne=}")
                direction = ligne[0]
                value = int(ligne[1:])
                verbose and print(f"{direction=}, {value=}")

                if value == 0:
                    raise ValueError("value ne peut pas être 0")

                if direction == 'L':
                    nb_passage_zero = value // 100
                    reste = value % 100
                    if reste >= actual_value:
                        if last_value_is_zero:
                            last_value_is_zero = False
                        else:
                            nb_passage_zero += 1

                    zero_count += nb_passage_zero
                    actual_value = (actual_value - value) % 100

                elif direction == 'R':
                    nb_passage_zero = (actual_value + value) // 100

                    zero_count += nb_passage_zero
                    actual_value = (actual_value + value) % 100
                verbose and print(f"{actual_value=}")

                if not (0 <= actual_value < 100):
                    raise ValueError("actual_value hors limites")

                if actual_value == 0:
                    last_value_is_zero = True
                else:
                    last_value_is_zero = False
        return zero_count


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)

# 15503 is too high
# 6586 is ??? but no correct
# 5836 is ??? but no correct
# 5927 is ??? but no correct
# 6195 is ??? but no correct
# 6734 is ??? but no correct
# 6175 IS CORRECT !
