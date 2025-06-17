#El usuario tiene 5 intentos para adivinar una palabra secreta. Si la acierta, gana. Si se acaban los intentos, pierde. La palabra se puede hardcodear.

secreta = "python"
intentos = 5

while intentos > 0:
    palabra = input("Adiviná la palabra secreta: ").lower()
    if palabra == secreta:
        print("¡Correcto! Ganaste.")
        break
    else:
        intentos -= 1
        print(f"Incorrecto. Intentos restantes: {intentos}")
else:
    print("Perdiste. La palabra era:", secreta)
