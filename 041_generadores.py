def pares(): # generador -> lazy iterator
    for numero in range(0, 12, 2):
        yield numero
        print('Se reanuda la ejecución')

# print(pares())

# for par in pares():
#    print(par)

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizó.')
        break