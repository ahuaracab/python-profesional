diccionario_variado = {'Angelo':(1, 2), True :[1, 2], 1.23:{'a':1}}
print(diccionario_variado)

#recomendable usar mismo tipo para las keys, generalmente string
diccionario = {'Angelo':1, 'Jose':2, 'Frank':3}
diccionario.keys()

#crear diccionario
diccionario_creado = dict()
#agregar nueva llave: valor
diccionario_creado['usuario'] = 'Angelo'
#actualizar valor mediante llave
diccionario_creado['usuario'] = 'ahuaracab'
#obtener valor mediante una llave
print(diccionario_creado['usuario'])

print(diccionario.keys()) # obtener llaves
print(tuple(diccionario.keys()))
print(diccionario.values()) # obtener valores
print(tuple(diccionario.values()))
print(diccionario.items()) # obtener key y value
print(tuple(diccionario.items()))


# obtener key y value
for key, value in diccionario.items():
    print(key, value)

usuario = {
    'name': 'Angelo Huaraca',
    'age': 28,
    'job': 'QAmaniaTIC'
}

calificaciones = usuario.get('calificaciones',[]) # mandar lista vacía para evitar error
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)

usuarios = ['Angelo', 'José', 'Frank']
diccionario_usuarios = {usuario:position+1
for position, usuario in enumerate(usuarios)}

print(diccionario_usuarios)

elementos = {}

elementos['nombre'] = 'Angelo'
elementos['apellido'] = 'Huaraca'

print(elementos)
print(len(elementos))

elementos['nombre'] = 'Michael'
print(elementos)

elementos_2 = {'a': 1, 'b': 2, 'a':4}
print(elementos_2)

elementos_3 = {'a': 1, 'b': 2, 'c':4}
print('a' in elementos_3) # si la llave existe o no en el diccionario
valor = elementos_3['a']
print(valor)

# get
valor_2 = elementos_3.get('z','La llave no existe en el diccioanrio') # retorna None, pero puede ponerse lo que devuelve por deafult si no existe
valor_3 = elementos_3.get('b','La llave no existe en el diccioanrio') 
print(valor_2)
print(valor_3)

# setdefault: agrega elemento si no existe llave
valor_4 = elementos_3.setdefault('e','5')
print(elementos_3)

# eliminar elementos de diccionario
print(len(elementos_3))
del elementos_3['a']
valor_pop = elementos_3.pop('b')
print(valor_pop)
print(elementos_3)
print(len(elementos_3))

elementos_3.clear()
print(elementos_3)
print(len(elementos_3))





