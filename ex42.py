numero = int(input("Introdueix un número entre 1 i 900000: "))

while numero < 1 or numero > 900000:
    numero = int(input("Introdueix un número vàlid: "))

print("Quantitat de dígits:", len(str(numero)))