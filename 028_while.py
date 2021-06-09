numero = 1234
contador_digitos = 0

while numero >= 1:
    contador_digitos += 1
    numero /= 10
else: 
    print('Fin del ciclo while')

print(contador_digitos) 
