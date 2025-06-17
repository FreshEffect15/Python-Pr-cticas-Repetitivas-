#Generá un número aleatorio entre 1 y 100. El usuario debe adivinarlo, y el programa le dará pistas de si el número es mayor o menor. Cuando lo adivine, mostrar en cuántos intentos lo logró.

import random

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        adivinado = True
    elif intento < secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
