def concatenar(llista1, llista2, connector):
    return [a + connector + b for a, b in zip(llista1, llista2)]


print(concatenar(["sub", "supra"], ["campió", "campiona"], "-"))