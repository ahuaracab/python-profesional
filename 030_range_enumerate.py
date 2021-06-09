# range
rango = range(11)
print(rango)
print(type(rango))

for numero in rango:
    print(numero)

rango2 = range(1,10,2)

for numero2 in rango2:
    print(numero2)

numeros = [10, 20, 30, 40]

# enumerate
for indice, numero in enumerate(numeros):
    print(indice, numero)