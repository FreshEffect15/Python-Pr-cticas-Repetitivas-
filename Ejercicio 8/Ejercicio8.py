#Pedile al usuario un número entero N y mostrá todos los números primos desde el 1 hasta N.

N = int(input("Ingrese un número: "))
for num in range(1, N + 1):
    if num < 2:
        continue
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")