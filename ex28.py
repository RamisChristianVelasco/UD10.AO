def filtrar_paraules(llista, x):
    return [paraula for paraula in llista if len(paraula) > x]


print(filtrar_paraules(["Hola", "Programació", "IES", "Python"], 4))