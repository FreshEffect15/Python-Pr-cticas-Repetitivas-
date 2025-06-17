#Permití al usuario ingresar números indefinidamente. El ciclo termina cuando la suma de los números supere 100. Mostrá la cantidad de números ingresados y la suma final.

suma = 0
contador = 0

while suma <= 100:
    num = float(input("Ingrese un número: "))
    suma += num
    contador += 1

print(f"Suma total: {suma}")
print(f"Números ingresados: {contador}")
