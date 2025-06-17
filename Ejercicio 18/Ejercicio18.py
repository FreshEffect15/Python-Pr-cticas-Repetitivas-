#Pedí al usuario un número N y generá un patrón como un tablero de ajedrez de tamaño N x N usando # y espacio en blanco ( ) alternados.

N = int(input("Ingrese el tamaño del tablero: "))

for i in range(N):
    fila = ""
    for j in range(N):
        if (i + j) % 2 == 0:
            fila += "#"
        else:
            fila += " "
    print(fila)