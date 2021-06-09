def suma_dos_numeros(numero1, numero2):
    return numero1 + numero2, 'La funcion retorna dos valores' # retorna una tupla

numero_uno = int(input('Ingresa el primer número entero: '))
numero_dos = int(input('Ingresa el primer número entero: '))
    
resultado, mensaje = suma_dos_numeros(numero_uno,numero_dos)
print('El resultado es:', resultado)
print(mensaje)