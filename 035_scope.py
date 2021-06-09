# scope
animal = 'León' # variable global -> función, condición o ciclo

def imprimir_animal():
    animal = 'Ballena' # variable local -> dentro del bloque donde fue creada
    tipo = 'Mamífero'
    print(animal)
    print(id(animal))

def imprimir_animal_2():
    global animal
    animal = 'Delfín'


imprimir_animal()
print(animal)
print(id(animal))

# print(tipo) # da error de tipo no definido

imprimir_animal_2()
print(animal)
print(id(animal))
