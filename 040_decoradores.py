"""
a -> función principal (decorador)
b -> función a decorar
c -> función decorada

a(b) -> c
"""

def funcion_a(funcion_b):
    
    def funcion_c(*args,**kwargs):
        print('Antes del llamado')
        resultado = funcion_b(*args,**kwargs)
        print('Despues del llamado')
        return resultado
        
    return funcion_c


@funcion_a
def saludar(): #funcion principal que no se puede modificar directamente
    print('Hola, mundo!')

saludar()

@funcion_a
def suma(numero_1, numero_2): #funcion principal que no se puede modificar directamente
    return numero_1 + numero_2

resultado = suma(10, 20)
print(resultado)
