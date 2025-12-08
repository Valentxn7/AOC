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
        list_number: list[list[object]] = list()
        for ligne in f:
            # verbose and print(f"Ligne non traitée : {ligne=}")
            ligne = ligne.split()
            verbose and print(f"Ligne traitée : {ligne=}")
            list_number.append(ligne)

            if ligne.__contains__("+") or ligne.__contains__("*"):
                verbose and print(f"Opérateur ! {list_number=}")
                break

        sum_result = 0
        while len(list_number[0]) > 0:
            result_memory = []
            for ligne in list_number:
                elt = ligne.pop()
                verbose and print(f"{elt=}")
                if elt == "+":
                    verbose and print(f"calculating addition of {result_memory}...")
                    result = 0
                    for number in result_memory:
                        result += number
                    verbose_vict and print(f"adding {result} to sum_result")
                    sum_result += result
                    verbose and print(f"{sum_result=}")
                elif elt == "*":
                    verbose and print(f"calculating multiplication of {result_memory}...")
                    result = 1
                    for number in result_memory:
                        result *= number
                    verbose_vict and print(f"adding {result} to sum_result")
                    sum_result += result
                    verbose and print(f"{sum_result=}")
                else:
                    verbose and print(f"memorizing {elt}...")
                    result_memory.append(int(elt))
        return sum_result


if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
