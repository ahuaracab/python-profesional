def centigrados_a_fahrenheit(grados):
    return grados * 1.8 + 32


"""
print(centigrados_a_fahrenheit(10))
print(centigrados_a_fahrenheit(-1))
print(centigrados_a_fahrenheit(8))
"""
mi_funcion = centigrados_a_fahrenheit # asignar funcion a variable mediante nombre de funcion sin parametros
print(type(mi_funcion))

print(mi_funcion(10))

funcion_grados = lambda grados : grados * 1.8 + 32
# lambda <parametros> : <cuerpo de la función>

print(funcion_grados(30))

sin_parametros = lambda : True
print(sin_parametros())

parametros_default = lambda p1=10, p2=20 : p1 + p2 
print(parametros_default())

asterisco = lambda *args, **kwargs : len(args) + len(kwargs)
print(asterisco(10, 30, 50, nombre='angelo', edad=28))