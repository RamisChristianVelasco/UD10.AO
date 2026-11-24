numero = int(input("Introdueix un número entre 1 i 20: "))

while numero < 1 or numero > 20:
    numero = int(input("Introdueix un número entre 1 i 20: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)