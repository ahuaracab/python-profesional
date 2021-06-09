nombre = 'Angelo'
apellido = 'Huaraca'

nombre_completo = 'Mr. ' + nombre + ' ' + apellido + '.'
print(nombre_completo)

nombre_completo_2 = 'Mr. %s %s.' %(nombre,apellido)
print(nombre_completo_2)
print('Mr. %s %s.' %(nombre,apellido))

nombre_completo_3 = 'Mr. {} {}.'.format(nombre,apellido)
print(nombre_completo_3)

nombre_completo_4 = 'Mr. {v_nombre} {v_apellido}.'.format(v_apellido=apellido,v_nombre=nombre)
print(nombre_completo_4)

nombre_completo_5 = f'Mr. {nombre} {apellido}.' # FString, mejor generando nuevo string
print(nombre_completo_5)
print(f'Mr. {nombre} {apellido}.')

# sep por defecto con espacio, end por defecto con salto de línea
print('Mr.',nombre, apellido, sep=' ', end='.') 