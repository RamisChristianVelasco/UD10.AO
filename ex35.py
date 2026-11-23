def comptar_vocals(paraula):
    vocals = "aeiou"
    resultat = {}

    for vocal in vocals:
        resultat[vocal] = paraula.lower().count(vocal)

    return resultat


print(comptar_vocals("Ratapinyada"))
