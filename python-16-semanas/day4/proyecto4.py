from random import randint
import time

print("\t>>>>> El número secreto <<<<<")
nombre = input("\nIngresa tu nombre: ")

print(f"Bienvenido, {nombre}")
print("Ahora pensaré un número del 1 al 100...")
numero_secreto = randint(1, 100)
time.sleep(1.4)

print("¡Lo tengo!\nTienes 8 intentos para adivinar...")
time.sleep(1.4)
print("¡Comencemos!\n")

numero_usuario = -1
intentos = 0
while numero_usuario != numero_secreto:
    intentos += 1
    if intentos <= 8:
        numero_usuario = int(input("¿Qué número pensé?: "))
        if numero_usuario not in range(1, 101):
            print("INCORRECTO ¡Ese número no está permitido!")
        elif numero_usuario < numero_secreto:
            print("INCORRECTO ¡Ese número es MENOR al numero secreto!")
        elif numero_usuario > numero_secreto:
            print("INCORRECTO ¡Ese número es MAYOR al numero secreto!")
        elif numero_usuario == numero_secreto:
            print(f"CORRECTO. ¡Te ha tomado {intentos} intentos, pero {numero_secreto} es el número secreto!")
    else:
        print("Ups. No tienes más intentos...")
        break

print("¡Hasta luego!")
