#Permití que el usuario cree una contraseña. Luego, pedí que la reingrese hasta que coincida con la original. Mostrá un mensaje de éxito al final.

clave = input("Cree una contraseña: ")
intento = input("Reingrese la contraseña: ")

while intento != clave:
    print("Contraseña incorrecta. Intente de nuevo.")
    intento = input("Reingrese la contraseña: ")

print("¡Contraseña confirmada con éxito!")