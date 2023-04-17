def reducir_lista(numeros):
    aux = list(set(numeros))
    aux.pop()
    return aux


def promedio(lista):
    return sum(lista) / len(lista)


lista_numeros = [1, 2, 15, 7, 2]
