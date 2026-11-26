num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

inici = min(num1, num2)
final = max(num1, num2)

suma = sum(range(inici, final + 1))

print("La suma és:", suma)