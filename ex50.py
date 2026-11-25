import random


def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]


llista = llista_20_elements()

print(llista)
print("Hi ha duplicats:", len(llista) != len(set(llista)))

