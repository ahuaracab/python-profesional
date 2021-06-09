def promedio_lista(listado): # recibe una lista
    return sum(listado) / len(listado)


def promedio_tupla(*args): # por convención args para pasar tupla
    print(args) 
    print(type(args))
    return sum(args) / len(args)


def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

lista = [10, 20, 30, 40]
resultado_lista= promedio_lista(lista)
print(resultado_lista)

resultado2 = promedio_tupla(10, 20, 30, 40)
print(resultado2)

combinacion(10, 20, 30, 40, 50, 60, p4=1000)

def usuarios(**kwargs): # por conveción kwargs para pasar diccionario
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])

def tupla_diccionario(p1=10, *args, p5=900, **kwargs): # no pueden ir parámetros después de **kwargs
    print(p1)
    print(args)
    print(p5)
    print(kwargs)
   

tupla_diccionario(5, 1, 2, 3 , p5=300, cody=True, curso='Python')