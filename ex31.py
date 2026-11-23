any_actual = int(input("Introdueix l'any actual: "))

for i in range(4):
    nom = input("Introdueix el nom: ")
    naixement = int(input("Introdueix l'any de naixement: "))
    edat = any_actual - naixement

    print(nom, "\t", naixement, "\t", edat)