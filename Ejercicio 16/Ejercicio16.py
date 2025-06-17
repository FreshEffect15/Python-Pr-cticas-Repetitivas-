#Escribí un programa que determine si un número ingresado por el usuario es capicúa (se lee igual al derecho y al revés).

numero = input("Ingrese un número: ")
if numero == numero[::-1]:
    print("El número es capicúa.")
else:
    print("El número NO es capicúa.")