def menu():
    opcio=0
    while(opcio<1 or opcio>4):
        print("""
        Menu principal:
        1. Suma
        2. Resta
        3. Multiplicació
        4. Divisió
        """)
        opcio = int(input("Indiqui el número de la funció que vol executar:"))
    return opcio

# Programa principal

op =menu()
match(op):
    case 1:
        print("Operacions de suma: ")
        x = int(input("Intro el 1r num: "))
        y = int(input("Intro el 2n num: "))
        print("La suma de {} i {} és {}".format(x, y, x + y))
    case 2:
        print("Operacions de resta: ")
        x = int(input("Intro el 1r num: "))
        y = int(input("Intro el 2n num: "))
        print("La resta de {} i {} és {}".format(x, y, x - y))
    case 3:
        print("Operacions de multiplicació: ")
        x = int(input("Intro el 1r num: "))
        y = int(input("Intro el 2n num: "))
        print("La multiplicació de {} i {} és {}".format(x, y, x * y))
    case 4:
        print("Operacions de divisió: ")
        x = int(input("Intro el 1r num: "))
        y = int(input("Intro el 2n num: "))
        print("La divisió de {} i {} és {}".format(x, y, x / y))
    case _:
        print("En qualsevol altre cas")
