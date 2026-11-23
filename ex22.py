def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False


print(superposicio([1, 2, 3], [4, 5, 3]))
print(superposicio([1, 2], [3, 4]))