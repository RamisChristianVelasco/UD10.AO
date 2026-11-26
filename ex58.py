def elements_parells(llista):
    for index, paraula in enumerate(llista):
        if index % 2 == 0:
            print(paraula)


elements_parells(["casa", "cotxe", "taula", "cadira", "porta"])
