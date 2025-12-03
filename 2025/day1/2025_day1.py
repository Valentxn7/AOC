with open("2025_day1_data", "r", encoding="utf-8") as f:
    nbLigne = 0
    actual_value = 50
    zero_count = 0
    verbose = True
    for ligne in f:
        if ligne != "":  # derniere ligne vide
            nbLigne = nbLigne + 1
            # print(f"Ligne entière : {ligne=}")
            ligne = ligne[:-1]
            # print(f"Ligne traitée : {ligne=}")
            direction = ligne[0]
            value = int(ligne[1:])
            print(f"{direction=}, {value=}")

            if direction == 'L':
                if value <= actual_value:
                    verbose and print("<=")
                    actual_value = actual_value - value
                else:
                    verbose and print(f"{value} - {actual_value}")
                    value = value - actual_value
                    verbose and print(f"Valeur restante à soustraire: {value=}")
                    actual_value = 100 - (value % 100)
                    if actual_value == 100:
                        actual_value = 0

            elif direction == 'R':
                if actual_value + value <= 99:
                    verbose and print(f"{value} + {actual_value}")
                    actual_value = actual_value + value
                else:
                    actual_value = actual_value + value
                    actual_value = actual_value % 100

            if actual_value == 0:
                print("ZERO DETECTED")
                zero_count = zero_count + 1
            verbose and print(f"{actual_value=}")
    verbose and print(f"{nbLigne=}")
    print(f"{zero_count=}")
