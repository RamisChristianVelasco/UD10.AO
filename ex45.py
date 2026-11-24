numero = input("Introdueix un número: ")

suma = sum(int(digit) for digit in numero)

print("Suma dels dígits:", suma)

if suma % 2 == 0:
    print("La suma és parell")
else:
    print("La suma és senar")

