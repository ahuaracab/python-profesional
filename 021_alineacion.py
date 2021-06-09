mensaje = 'Hola mundo!'
# ljust -> justificar a la izquierda
# rjust -> justificar a la derecha
# center -> centrar

#argumento representa espacio ocupado, incluido espacios
print(mensaje.ljust(20),'.',sep='')
print(mensaje.rjust(20))
print(mensaje.center(19),'.',sep='')