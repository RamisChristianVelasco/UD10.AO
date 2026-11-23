def nums_que_comencen_per(llista):
    comptador = 0

    for nom in llista:
        if nom.lower().startswith("a"):
            comptador += 1

    return comptador


noms = ["Anna", "Pere", "Antoni", "Maria"]
print(nums_que_comencen_per(noms))
