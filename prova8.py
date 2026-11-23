# Llegim 5 elements, després els imprimim com una cadena de caràcters
#l = list()
#for i in range(5):
  #  a = input("Intro un número: ")
 #   l.append(a)
#print(",".join(l))

# Llegir 5 noms, i només imprimir els que no tenen la lletra 'a' o 'A'
#l=list()
#for i in range(5):
 #   l.append(input("Intro un nom: "))
#for e in l:
#    if "a" not in e and "A" not in e:
 #       print(e)

# # Llegir 5 noms, i només imprimir els que no tenen la lletra 'a', 'A' o 's' o 'S'
l=list()
for i in range(5):
    a = input("Intro un nom: ")
    l.append(a)
for e in l:
    if ("a" not in e) and ("s" not in e):
        print(e)


