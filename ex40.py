capital = float(input("Introdueix el capital inicial: "))

while capital < 50000 or capital > 800000:
    capital = float(input("Capital entre 50000 i 800000: "))

interes = float(input("Introdueix l'interès (%): "))

while interes < 0.5 or interes > 13:
    interes = float(input("Interès entre 0.5 i 13: "))

anys = int(input("Introdueix el nombre d'anys: "))

while anys < 3 or anys > 40:
    anys = int(input("Anys entre 3 i 40: "))

capital_final = capital * (1 + interes / 100) ** anys

print("Capital final:", round(capital_final, 2), "€")