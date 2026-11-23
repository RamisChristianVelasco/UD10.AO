def comptar_majuscules(cadena):
    comptador = 0

    for lletra in cadena:
        if lletra.isupper():
            comptador += 1

    return comptador


print(comptar_majuscules("Hola BON DIA"))