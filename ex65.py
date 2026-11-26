def crear_diccionari(llista):
    return {valor: index for index, valor in enumerate(llista)}


print(crear_diccionari(["casa", "cotxe", "cadira", "taula"]))