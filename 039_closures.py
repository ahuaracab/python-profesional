e = 'e' # variable global

def funcion_principal():
    a = 'a' # variables locales
    b = 'b'

    def funcion_anidada():
        c = 'c' # variable local
        nonlocal b # para usar solo otra variable local, no global
        b = 'cambio de valor'        
        print(a)
        print(b)
        print(e)

    funcion_anidada()
    # print(c)
    print(b)

funcion_principal()

def saludar(username):
    mensaje = f'Hola {username}' # variable local
    
    def mostrar_mensaje(): # anidada
        print(mensaje)

    return mostrar_mensaje


username = 'Angelo'
respuesta = saludar(username)

username = 'Frank' # se sigue mostrando Angelo
respuesta()

