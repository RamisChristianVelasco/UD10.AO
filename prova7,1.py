l=list()
for i in range(3):
    l.append(int(input("Intro un número: ")))
l2 = list()
for i in range(len(l)):
    l2.append(l[i])
for i in range(2,-1, -1):
    l2.append(l[i])
print(l2)
