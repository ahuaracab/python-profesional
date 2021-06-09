titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'

contador_python = titulo_curso.count('Python')
contador_o = titulo_curso.count('o')

print(contador_python)
print(contador_o)

print('python' in titulo_curso) # diferencia mayusculas o minusculas
print('python' in titulo_curso.lower()) # diferencia mayusculas o minusculas
print('java' not in titulo_curso) # diferencia mayusculas o minusculas

print(titulo_curso.startswith('curso'))
print(titulo_curso.endswith('Python'))