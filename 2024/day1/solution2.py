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
    while liste_gauche:
        first_g = liste_gauche[0]
        occurrence = 0

        for elt in liste_droit:
            if elt == first_g:
                occurrence += 1

        somme += first_g * occurrence
        liste_gauche.remove(first_g)
    return result

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
