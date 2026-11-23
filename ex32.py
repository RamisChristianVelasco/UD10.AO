def mostrar_majors_que(tupla, numero):
    for valor in tupla:
        if valor > numero:
            print(valor)


valors = input("Introdueix números separats per espais: ")
tupla = tuple(map(int, valors.split()))

mostrar_majors_que(tupla, 18)