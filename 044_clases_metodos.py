class Usuario:
    
    #si no se pone __init__ tienes que invocar al método
    def __init__(self, username, password): # puede ser cualquiera, pero si es primero se recomienda self
        self.username = username
        self.password = password
        print('Se inicializó')


# user1 = Usuario()
# user2 = Usuario()

# user1.inicializar('user1','password1')
# user2.inicializar('user2','password2')

user1 = Usuario('user1','password1')
user2 = Usuario('user2','password2')

print(user1.__dict__)
print(user2.__dict__)

print(user1.username)
print(user1.password)
print(user2.username)
print(user2.password)


