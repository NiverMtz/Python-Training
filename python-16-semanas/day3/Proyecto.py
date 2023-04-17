def pedir_texto(message):
    return input(message).lower()


def contar_letras(cadena, lista):
    for letra in lista:
        print(f"La letra '{letra}' aparece {cadena.count(letra)} veces")


def contar_palabras(cadena):
    print(f"El texto tiene {len(cadena.split())} palabras")


def buscar_primera_ultima(cadena):
    last_char = cadena[-1]
    penul_char = cadena[-2]
    last_def_char = penul_char if last_char in ['.', ','] else last_char
    print(f"La primera letra es '{cadena[0]}' y la última es '{ last_def_char }'")


def invertir_texto(cadena):
    cadena_reversada = cadena.split()
    cadena_reversada.reverse()
    cadena_reversada = " ".join(cadena_reversada)
    print(cadena_reversada)


def buscar_palabra(cadena):
    dic = {True: 'Sí', False: 'No'}
    existe = "python" in cadena
    print(f"{dic[existe]} está la palabra 'Python'")


texto = pedir_texto("Ingrese su texto: ")
letras = [pedir_texto(f"Letra { item + 1 }: ") for item in range(0, 3)]

print("\n>> Análisis del texto <<\n")
print("1. Conteo de cada letra")
contar_letras(texto, letras)

print("\n2. Conteo de palabras")
contar_palabras(texto)

print("\n3. Primera y última letra")
buscar_primera_ultima(texto)

print("\n4. Inversión del texto")
invertir_texto(texto)

print("\n5. Buscar la palabra Python")
buscar_palabra(texto)
