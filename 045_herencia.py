class Animal:
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')

class Mascota(Animal):
    pass

class Felino:
    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino):
    pass

gato1 = Gato()

gato1.comer()
gato1.dormir()
gato1.cazar()
