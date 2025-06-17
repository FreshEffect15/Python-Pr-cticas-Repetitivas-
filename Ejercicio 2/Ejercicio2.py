# Hacé un programa que permita ingresar números hasta que el usuario ingrese 0. Luego, mostrá la suma de todos los números ingresados.

suma = 0
num = int(input("Ingrese un número (0 para terminar): "))
while num != 0:
    suma += num
    num = int(input("Ingrese otro número (0 para terminar): "))
print("Suma total:", suma)