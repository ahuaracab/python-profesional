class Usuario: # nombre de la clase CamelCase y en singular
    # atributos de clase
    username = 'ahuaracab'
    email = ''
    

print(Usuario.username)
Usuario.username = 'Otro user'
Usuario.email = 'Otro email'
print(Usuario.username)
print(Usuario.email)

user1 = Usuario()
user2 = Usuario()
print(user1)
print(type(user1))

# __dict__
# 1. verifica si el atributo existe dentro del objeto
# 2. verifica si el atributo existe dentro de la clase -> lectura
# 3. lanza un error si no hay un atributo que exista
user1.username = 'Angelo' # añadimos el atributo al objeto 
user1.password = '123456'
user1.password = '456789'

print(user1.username) # se convierte en atributo de instancia
print(user1.email) # sigue siendo atributo de clase

print(user1.__dict__) # todos los atributos del objeto

print(id(Usuario.username))
print(id(user1.username))

print(user2.password)