import sys

liste_gauche = list()
liste_droit = list()

donnee = list()  # 0: GameX 1: liste des jeux

def get_num_of_name(game: str) -> int:
    return int(game[4:])

def solve(input_file):
    with open(input_file, 'r') as f:
        regle = [12, 13, 14]
        sum_game = 0
        # on upload tout le ficher
        for ligne in f:
            #print(f"Ligne entière : {ligne=}")
            ligne = ligne[:-1]
            #print(f"Ligne traitée : {ligne=}")
            # on sépare Game X au reste des données
            datas = ligne.split(":")

            data_gauche = datas[0]  # Game X
            data_droite = datas[1][1:]  # tout les jeux séparé par ;

            #print(f"{data_gauche=}, {data_droite=}")

            data_droite_separee = data_droite.split(";")

            #print(f'{data_droite_separee=}')
            for i in range(0, len(data_droite_separee)):
                data_droite_separee[i] = data_droite_separee[i].strip()

            #print(f'data_droite_separee_stripped={data_droite_separee}')

            all_data_droite_prepared = []

            liar = False
            for data_droite in data_droite_separee:
                one = ["None", "None", "None"]  # R G B
                #print(f"{data_droite=}")
                splitted = data_droite.split(",")
                for elt in splitted:
                    if elt[-1] == "d":  # Red
                        one[0] = int(elt[:-4].strip())
                        if one[0] > regle[0]:
                            #print(f"passed !")
                            liar = True
                            break
                    if elt[-1] == "n":  # Green
                        one[1] = int(elt[:-6].strip())
                        if one[1] > regle[1]:
                            #print(f"passed !")
                            liar = True
                            break
                    if elt[-1] == "e":  # Blue
                        one[2] = int(elt[:-5].strip())
                        if one[2] > regle[2]:
                            #print(f"passed !")
                            liar = True
                            break
                    all_data_droite_prepared.append(one)

                if liar:
                    break
                #print(f"{one=}")
                all_data_droite_prepared.append(one)

            if not liar:
                donnee.append([data_gauche, all_data_droite_prepared])
                num_game = get_num_of_name(data_gauche)
                sum_game = sum_game + get_num_of_name(data_gauche)
                #print(f"ajouté à la somme: {num_game=}, {sum_game=}")

        #print(f"{donnee=}")
        #print(f"{sum_game=}")
        return sum_game

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)