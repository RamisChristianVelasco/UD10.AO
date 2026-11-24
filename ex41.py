numero = int(input("Introdueix un número menor de 100: "))

if 0 < numero < 100:
    suma = 0

    for valor in range(numero - 4, 0, -4):
        suma += valor ** 2

    print("Suma dels quadrats:", suma)
else:
    print("El número ha de ser entre 1 i 99")