def sumar_llista(llista):
    return sum(llista)


def multiplicar_llista(llista):
    resultat = 1

    for numero in llista:
        resultat *= numero

    return resultat


print(sumar_llista([1, 2, 3, 4]))
print(multiplicar_llista([1, 2, 3, 4]))