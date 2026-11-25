def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))


print(hi_ha_duplicats([1, 2, 3, 4]))
print(hi_ha_duplicats([1, 2, 2, 4]))
