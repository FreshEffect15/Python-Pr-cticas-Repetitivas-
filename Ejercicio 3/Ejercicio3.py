#Pedí al usuario un número entero positivo e imprimí su tabla de multiplicar del 1 al 10.

n = int(input("Ingrese un número entero positivo: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")