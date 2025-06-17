#Permití ingresar hasta 10 números. Solo se suman los positivos. Si el usuario ingresa un número negativo, ese número no se suma y se repite el turno. Mostrá la suma total al final.

suma = 0
ingresados = 0

while ingresados < 10:
    n = float(input(f"Ingrese el número {ingresados + 1}: "))
    if n < 0:
        print("Número negativo. Intente de nuevo.")
        continue
    suma += n
    ingresados += 1

print("Suma total de números positivos:", suma)