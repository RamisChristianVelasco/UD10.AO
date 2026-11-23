def es_de_traspas(any):
    return any % 400 == 0 or (any % 4 == 0 and any % 100 != 0)


any = int(input("Introdueix un any: "))

if es_de_traspas(any):
    print("És un any de traspàs")
else:
    print("No és un any de traspàs")
