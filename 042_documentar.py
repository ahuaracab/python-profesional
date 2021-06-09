# Docstring
# __doc__ (módulos, clases, métodos, funciones)

def suma(numero_1, numero_2):
    """
    La funcion suma dos números enteros.
    
    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parámetros.

    >>> suma(10, 20)
    30

    >>> suma(40, -20)
    20

    """
    return numero_1 + numero_2

# print(suma.__doc__)
# print(help(suma))

def resta(numero_1, numero_2):
    """
    La funcion suma dos números enteros.
    
    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la resta de los parámetros.

    >>> resta(10, 20)
    -10

    >>> resta(30, -20)
    60

    """
    return numero_1 - numero_2