lenguajes = 'Python Ruby Java Rust C++ C'
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

lenguajes_2 = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes_2 = lenguajes_2.split('-')
print(listado_lenguajes_2)

lenguajes_3 = 'Python/*/Ruby/*/Java/*/Rust/*/C++/*/C'
listado_lenguajes_3 = lenguajes_3.split('/*/', 2)
print(listado_lenguajes_3)

string_lenguajes = '&'.join(listado_lenguajes_2)
print(string_lenguajes)
print(type(string_lenguajes))