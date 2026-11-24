paraula1 = input("Introdueix la primera paraula: ").lower()
paraula2 = input("Introdueix la segona paraula: ").lower()

if paraula1[-3:] == paraula2[-3:]:
    print("Rimen")
elif paraula1[-2:] == paraula2[-2:]:
    print("Rimen un poc")
else:
    print("No rimen")