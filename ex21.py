def es_palindrom(paraula):
    paraula = paraula.lower().replace(" ", "")
    return paraula == paraula[::-1]


print(es_palindrom("radar"))
print(es_palindrom("hola"))
print(es_palindrom("anna"))