def comptar_coincidencies(llista):
    comptador = 0

    for index, valor in enumerate(llista):
        if index == valor:
            comptador += 1

    return comptador


print(comptar_coincidencies([0, 2, 3, 3, 4]))

