binari = input("Introdueix un número binari: ")

if all(digit in "01" for digit in binari):
    decimal = int(binari, 2)
    print("Número decimal:", decimal)
else:
    print("El número introduït no és binari")