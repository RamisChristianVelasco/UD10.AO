l=list()
for i in range(5):
    l.append(int(input("Intro un número: ")))
l2 = list()
for i in range(len(l)):
    l2.append(l[i])
for i in range(4,-1, -1):
    l2.append(l[i])
print(l2)
# Sumar tots els elements de la llista

#suma = 0
#for e in l:
#    suma = suma + int(e)

#print("La suma d tots els elemenets de la llista és: {}".format(suma))

# A cada element de la llista sumar un número llegit per teclat

#num = int(input("Intro un número a sumar a cada element de la llista: "))
#for i in range(len(l)):
#     l[i] = (l[i]) + num
#for e in l:
#    print(e)

# Llegim 5 elements del teclat

