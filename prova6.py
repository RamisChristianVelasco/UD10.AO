l=[1, 2, [2, 3], "Hola"]
lf = ["a", 2, [2, 3], "Hola"]
l[3]="Hala"
#print(l[::-1])
for e in l:
    print(e)
for i in range(len(l)):
    print(i)
    if l[i]==1 or l[i]=="1":
        l[i]="a"
for i,e in enumerate(l):
    print("La posició {} val {}".format(i, e))
    if e == 1 or e == "1":
        l[i]="a"
for e in l:
    print(e)
    if l[i]==2 or l[i]=="2":
        l[i]="b"
        