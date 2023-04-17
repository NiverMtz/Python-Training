from random import choice


def lanzar_moneda():
    return choice(["Cara", "Cruz"])


def probar_suerte(lado_moneda, lista):
    if lado_moneda == "Cara":
        print("La lista se autodestuirá")
    else:
        print("La lista fue salvada")
    return [n for n in lista if lado_moneda == "Cruz"]


lista_numeros = [1, 3, 5]

