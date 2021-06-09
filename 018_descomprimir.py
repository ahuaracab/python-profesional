numeros = (1, 2, 3, 4, 5, 6, 7, 8)
uno, _, tres, cuatro, *resto_valores, ocho = numeros

# _ omite el elemento
# * agrupa elementos que no se descomprimen
print(uno)
print(tres)
print(cuatro)
print(resto_valores) #imprime una lista
print(ocho)

