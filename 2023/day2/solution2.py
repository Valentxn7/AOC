import sys

liste_gauche = list()
liste_droit = list()

donnee = list()  # 0: GameX 1: liste des jeux

def get_num_of_name(game: str) -> int:
    return int(game[4:])

def solve(input_file):
    sum_power = 0
    with open(input_file, 'r') as f:
        for ligne in f:
            print(f"Ligne entière : {ligne=}")
            ligne = ligne[:-1]
            print(f"Ligne traitée : {ligne=}")
            # on sépare Game X au reste des données
            datas = ligne.split(":")

            data_gauche = datas[0]  # Game X
            data_droite = datas[1][1:]  # tout les jeux séparé par ;

            print(f"{data_gauche=}, {data_droite=}")

            data_droite_separee = data_droite.split(";")

            print(f'{data_droite_separee=}')
            for i in range(0, len(data_droite_separee)):
                data_droite_separee[i] = data_droite_separee[i].strip()

            print(f'data_droite_separee_stripped={data_droite_separee}')

            all_data_droite_prepared = []

            liar = False
            max_r = 1
            max_g = 1
            max_b = 1
            for data_droite in data_droite_separee:
                one = ["None", "None", "None"]  # R G B
                print(f"{data_droite=}")
                splitted = data_droite.split(",")
                for elt in splitted:
                    if elt[-1] == "d":  # Red
                        one[0] = int(elt[:-4].strip())
                        if one[0] > max_r:
                            max_r = one[0]
                    if elt[-1] == "n":  # Green
                        one[1] = int(elt[:-6].strip())
                        if one[1] > max_g:
                            max_g = one[1]
                    if elt[-1] == "e":  # Blue
                        one[2] = int(elt[:-5].strip())
                        if one[2] > max_b:
                            max_b = one[2]
                    all_data_droite_prepared.append(one)

                print(f"{one=}")
                all_data_droite_prepared.append(one)

            donnee.append([data_gauche, all_data_droite_prepared])
            power_game = max_r * max_g * max_b
            sum_power = sum_power + power_game
            print(f"ajouté au pouvoir: {power_game=}, {sum_power=}")

        print(f"{donnee=}")
        print(f"{sum_power=}")
        return sum_power

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)