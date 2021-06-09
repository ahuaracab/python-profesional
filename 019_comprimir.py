lista = [1, 2, 3, 4, 5, 6]
tupla = (10, 20, 30, 40, 50)

resultado1 = zip(lista,tupla) #retorna objeto tipo zip
resultado2 = zip(tupla,lista) #retorna objeto tipo zip

resultado_tupla = tuple(resultado1)
print(resultado_tupla)

resultado_tupla = tuple(resultado2)
print(resultado_tupla)

resultado_lista = list(resultado1)
print(resultado_lista)