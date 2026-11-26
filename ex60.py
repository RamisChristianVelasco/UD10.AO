primers = []

for numero in range(2, 101):
    es_primer = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primer = False
            break

    if es_primer:
        primers.append(numero)

print("Números primers:", primers)
print("Quantitat:", len(primers))

