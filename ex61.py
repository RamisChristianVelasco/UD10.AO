from functools import reduce


def lenp(frase):
    paraules = frase.split()
    return list(map(len, paraules))


print(lenp("Hola com estàs avui"))

