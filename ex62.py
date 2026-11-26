from functools import reduce


def passar_a_numero(llista):
    return reduce(lambda total, digit: total * 10 + digit, llista)


print(passar_a_numero([3, 4, 1, 5]))

