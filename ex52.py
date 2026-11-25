def crear_llista_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as fitxer:
            contingut = fitxer.read()
            return contingut.split()
    except FileNotFoundError:
        print("El fitxer no existeix")
        return []
    except OSError:
        print("No s'ha pogut obrir el fitxer")
        return []


print(crear_llista_fitxer("paraules.txt"))

