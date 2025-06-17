#Dado un número N, mostrará un triángulo invertido de asteriscos.

N = int(input("Ingrese la altura del triángulo: "))
for i in range(N, 0, -1):
    print("*" * i)