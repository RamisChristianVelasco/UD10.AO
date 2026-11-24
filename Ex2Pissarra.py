# Llegir 10 noms i juntar-los de 2 en dos i llavors imprimir

l = []
for i in range(10):
    l.append(input("Introdueix un nom: "))
r= list()

for i in range(0, 10, 2):
    r.append(l[i] + " " + l[i+1])
r2 = list()

for i in range(9, 0, -2):
    r2.append(l[-(i+1)]+" "+l[i])
print(r2)

for j in range(1, 10, 2):
    print(j)



# Leer 10 números y guardarlos en una lista. Después crer una nueva lista con sus cuadrados. Imprimir los números y al lado su cuadrado.

l = list()
for i in range(10):
    l.append(int(input("Introdueix un número: ")))

r = list()
for x in l:
    r.append(x**2)

for i in range(10):
    print(f"{l[i]} - {r[i]}")

