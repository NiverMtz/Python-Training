mi_lista = ['g', 'a', 'b', 'c']

print(mi_lista)

aux = "#".join(mi_lista)
mi_lista.sort()

lista_original = aux.split("#")

print(mi_lista)
print(lista_original)