# Llegir 10 nombres (Dins una llista), després sumar els de les posicions parells i imprimir el resultat

l = list()

for i in range(10):
    l.append(input["Nombre: "])

suma = 0 

for i in range(0, 10, 2):
    suma = suma + l[i]
print(suma)

