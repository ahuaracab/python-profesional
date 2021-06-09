lista = [8, 19, 102, 15, 9, 104, 32, 9]
print(9 in lista)

index = lista.index(9)
print(index)

lista.sort()
print(lista)
print(lista[0]) # min
print(lista[-1]) # max

print(min(lista))
print(max(lista))

lista.sort(reverse=True)
print(lista)



