from random import randint


def devolver_distintos(*args):
    args = sorted(args[0])
    suma = sum(args)
    if suma in range(1, 10):
        return min(args)
    elif suma in range(10, 16):
        return args[1]
    else:
        return max(args)


lista_numeros = [randint(1, 10), randint(1, 10), randint(1, 10)]
print(lista_numeros)
resultado = devolver_distintos(lista_numeros)
print(resultado)
