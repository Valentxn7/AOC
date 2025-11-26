import sys

liste_gauche = list()
liste_droit = list()

# on upload tout le ficher
with open("2024_day1_data", "r", encoding="utf-8") as f:
    for ligne in f:
        print(f"Ligne entière : {ligne=}")
        ligne = ligne[:-1]
        print(f"Ligne traitée : {ligne=}")
        # on sépare la colonne de gauche et de droite, chacune dans sa liste respective
        datas = ligne.split("   ")
        data_gauche = datas[0]
        data_droite = datas[1]

        print(f"{data_gauche=}, {data_droite=}")

        liste_gauche.append(int(data_gauche))
        liste_droit.append(int(data_droite))


def solve(input_file):
    somme = 0
    while liste_gauche and liste_droit:
        mini_g = min(liste_gauche)
        mini_d = min(liste_droit)

        diff = abs(mini_g - mini_d)
        somme += diff
        liste_gauche.remove(mini_g)
        liste_droit.remove(mini_d)

    print(f"{somme=}")
    return somme

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
