class Animal:

    def comer(self):
        print('El animal come.')


    def dormir(self):
        print('El animal duerme.')


class Mascota(Animal):
    def comer(self):
        print('La mascota come.')


class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino):

    def __init__(self, nombre):
        self.nombre = nombre

    def dormir(self):
        print(f'El gato {self.nombre} duerme.')

    def comer(self):
        super().comer()
        print(f'El gato {self.nombre} come.')

gato1 = Gato('Robert')

gato1.comer() # busca en su clase, luego en los padres de izquierda a derecha y así sucesivamente
gato1.dormir()
gato1.cazar()
