lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
print(len(lista_cursos))
lista_cursos_2 = ['C', 'C#', 'Docker']

primer_curso = lista_cursos[0]
print(primer_curso)

ultimo_curso = lista_cursos[4]
print(ultimo_curso)

ultimo_curso_alternativa = lista_cursos[-1]
print(ultimo_curso_alternativa)

lista_cursos[4] = 'Rust'
print(lista_cursos[4])

sub_lista_uno = lista_cursos[0:3] # no se toma índice final
print(sub_lista_uno)

sub_lista_dos = lista_cursos[:3] # no se toma índice final
print(sub_lista_dos)

sub_lista_tres = lista_cursos[2:] # no se toma índice final
print(sub_lista_tres)

sub_lista_cuatro= lista_cursos[1:-1] 
print(sub_lista_cuatro)

sub_lista_cinco= lista_cursos[1:-3] 
print(sub_lista_cinco)

sub_lista_seis= lista_cursos[0:5:2] # tercer parámetro: salto
print(sub_lista_seis)

sub_lista_seis= lista_cursos[::-1]
print(sub_lista_seis)

sub_lista_seis= lista_cursos[::-2] 
print(sub_lista_seis)

lista_cursos.append('MongoDB') # agregar elementos al final
lista_cursos.append('C#')
lista_cursos.append('JavaScript')
lista_cursos.insert(2,'Rails') # agregar elemento en índice específico
lista_cursos.insert(0,'PyGame')
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.extend(lista_cursos_2) # añadir lista en otra lista
print(lista_cursos)

lista_cursos.remove('MongoDB') # eliminar elemento por valor
print(lista_cursos)

del lista_cursos[0] # eliminar elemento por índice
print(lista_cursos)

lista_cursos.clear()
print(lista_cursos)