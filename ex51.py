def elimina_duplicats(llista):
    nova_llista = []

    for element in llista:
        if element not in nova_llista:
            nova_llista.append(element)

    return nova_llista


print(elimina_duplicats([1, 2, 2, 3, 4, 4, 5]))

