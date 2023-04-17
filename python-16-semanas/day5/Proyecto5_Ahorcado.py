from random import choice

palabras = ['nunc', 'non', 'molestie', 'nisl', 'cras', 'aliquet', 'posuere', 'felis', 'at', 'porta', 'suspendisse',
            'viverra', 'dui', 'varius', 'iaculis', 'venenatis', 'suspendisse', 'arcu', 'elit', 'elementum', 'a',
            'lorem', 'vitae', 'bibendum', 'commodo', 'orci', 'praesent', 'eu', 'erat', 'ac', 'mi', 'sollicitudin',
            'pulvinar', 'non', 'in', 'nunc', 'nunc', 'volutpat', 'dui', 'elit', 'efficitur', 'cursus', 'dolor',
            'vulputate', 'sollicitudin']
letras_incorrectas = []
vidas = 6


def elegir_palabra(lista):
    return choice(lista)


def mostrar_guiones(palabra):
    return ''.join(['_ ' for n in palabra])


def validar_entrada():
    letra = input("Ingresa una letra: ")
    letras_validas = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    while letra not in letras_validas or len(letra) > 1:
        letra = input("¡Ese no es un caracter válido!\nIngresa una letra: ")
    return letra


def validar_letra_oculta(palabra, letra, auxiliar):
    existe = letra in palabra
    if auxiliar == '':
        palabra_modificada = ''.join([e + ' ' if e == letra else '_ ' for e in palabra])
    else:
        palabra_modificada = ''.join([e + ' ' if e == letra or e in auxiliar else '_ ' for e in palabra])
    return palabra_modificada, existe


def mostrar_datos_jugador(lista_incorrectas, vidas_restantes):
    print(f"Letras incorrectas: {','.join(lista_incorrectas)}\nVidas: {vidas_restantes}")


def palabra_completa(palabra):
    return '_' not in palabra


print("🔴🟠😵🟢🔵 Juego del ahorcado 🔴🟠😵🟢🔵\n")
palabra_oculta = elegir_palabra(palabras)
print(f"Palabra: {mostrar_guiones(palabra_oculta)}\n------------------------------------")


palabra_aux = ''
while vidas > 0:
    letra_intento = validar_entrada()
    palabra_aux, acierto = validar_letra_oculta(palabra_oculta, letra_intento, palabra_aux)
    if acierto:
        print("✅✅✅✅✅ :)")
        print(f"Palabra oculta: {palabra_aux}")
        if palabra_completa(palabra_aux):
            print("\n🎉🎉🎉 Has ganado 🎉🎉🎉")
            break
    else:
        print("❌❌❌❌❌ :(")
        print(f"Palabra oculta: {palabra_aux}")
        if letra_intento not in letras_incorrectas:
            letras_incorrectas.append(letra_intento)
        vidas -= 1
        print("¡Has perdido una vida!")
    mostrar_datos_jugador(letras_incorrectas, vidas)
    print("------------------------------------")
else:
    print(f"\nLa palabra oculta era: {palabra_oculta}")
    print("\n💀💀💀 Game Over 💀💀💀")
