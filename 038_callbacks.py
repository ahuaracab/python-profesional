promedio = lambda *args : sum(args) / len(args)
aprobatorio = lambda calificacion : calificacion >= 7

print(promedio(7, 10, 9, 6))
print(aprobatorio(5))


def es_aprobatorio(calificacion):
    return calificacion >= 90


def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args) # * es para pasar los valores de la tupla
    if func_aprobatorio(promedio):
        print(f'Aprobaste la materia con {promedio}!')
    else:
        print('No aprobaste la materia!')


mostrar_mensaje(promedio, aprobatorio, 7, 10, 9, 6)
mostrar_mensaje(promedio, es_aprobatorio, 7, 10, 9, 6)