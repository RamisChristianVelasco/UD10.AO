import random

secret = "".join(str(random.randint(0, 9)) for _ in range(4))

while True:
    intent = input("Introdueix un codi de 4 xifres: ")

    if len(intent) != 4 or not intent.isdigit():
        print("Has d'introduir exactament 4 xifres")
        continue

    encertats = 0
    coincidencies = 0

    for i in range(4):
        if intent[i] == secret[i]:
            encertats += 1
        elif intent[i] in secret:
            coincidencies += 1

    if encertats == 4:
        print("Has encertat el codi!")
        break

    print("Números en la posició correcta:", encertats)
    print("Números que coincideixen en una altra posició:", coincidencies)