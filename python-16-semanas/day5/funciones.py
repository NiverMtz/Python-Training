from random import randint


# Simular lanzamiento de dados
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


# Evaluar la jugada según lanzamiento de dados
def evaluar_jugada(dado1, dado2):
    suma = dado1 + dado2
    if suma in range(1, 7):
        return f"La suma de tus dados es {suma}. Lamentable"
    elif suma in range(7, 10):
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"


dado1, dado2 = lanzar_dados()
evaluar_jugada(dado1, dado2)
