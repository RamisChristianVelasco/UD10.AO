def filtrar_paraules(llista, lletra):
    return list(filter(lambda paraula: paraula.lower().startswith(lletra.lower()), llista))


paraules = ["maria", "manta", "peu", "mà"]

print(filtrar_paraules(paraules, "p"))