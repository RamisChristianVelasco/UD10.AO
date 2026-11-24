import random


def intro():
    print("En una època on els gegants governen Menorca.")
    print("Has de trobar el talaiot dels gegants bons.")


def canviTalaiot():
    talaiot = ""

    while talaiot not in ("1", "2"):
        talaiot = input("A quin talaiot vols anar? Introdueix 1 o 2: ")

    return talaiot


def trobada(talaiot):
    gegantamic = str(random.randint(1, 2))

    if talaiot == gegantamic:
        print("Et convida a menjar!")
        return True
    else:
        print("Se't menja d'un mos... ÑAM ÑAM!")
        return False


punts = 0
partida_nova = "si"

while partida_nova.lower() in ("s", "si"):
    intro()
    talaiot = canviTalaiot()

    if trobada(talaiot):
        punts += 1
    else:
        break

    partida_nova = input("Vols tornar a jugar? ")

print("Punts aconseguits:", punts)