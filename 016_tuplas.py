from typing import Counter


tupla = ()
print(type(tupla))

#           0        1      2        3
tupla = ('String', True, [1,2,5], (4,5,6))
print(tupla)

lista_cursos = ('Python', 'Django', 'Flask', 'Ruby', 'Java')
print(lista_cursos)

# tuplas son más rápidas para consultar que las listas
primer_curso = lista_cursos[0]
print(primer_curso)

ultimo_curso = lista_cursos[-1]
print(ultimo_curso)

# sub-tuplas
sub_tupla = lista_cursos[0::2]
print(sub_tupla)