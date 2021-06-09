variable = '' or 'Huaraca'
# de izquierda a derecha
# la variable toma el primer True
print(variable)

variable_2 = '' or 0 or [] or True
print(variable_2)

listado = [1]
nombre = 'Cody'

if listado:
    variable = listado
else:
    variable = nombre
print(variable)

variable_3 = listado or nombre
print(variable_3)
