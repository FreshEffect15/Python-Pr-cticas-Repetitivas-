#Solicitá al usuario un número N y mostrá la serie de Fibonacci hasta que el valor más alto sea menor o igual

N = int(input("Mostrar la serie de Fibonacci hasta: "))

a, b = 0, 1
while a <= N:
    print(a, end=" ")
    a, b = b, a + b