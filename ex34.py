def nums_que_comencen_per(llista, lletra):
    comptador = 0

    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1

    return comptador


noms = ["Anna", "Pere", "Antoni", "Maria"]
lletra = input("Introdueix una lletra: ")

print(nums_que_comencen_per(noms, lletra))
