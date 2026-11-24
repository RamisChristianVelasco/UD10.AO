numero = input("Introdueix un número: ")

for digit in numero:
    if digit.isdigit() and int(digit) % 2 == 0:
        print(digit)

