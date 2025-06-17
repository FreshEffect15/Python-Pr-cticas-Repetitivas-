#Pedí al usuario un número entero positivo N y mostrá un triángulo rectángulo con N filas de asteriscos (*).

N = int(input("Ingrese la cantidad de filas: "))
for i in range(1, N+1):
    print("*" * i)