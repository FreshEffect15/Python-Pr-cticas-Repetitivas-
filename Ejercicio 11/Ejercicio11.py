#Solicitá dos números enteros a y b, donde a < b. Mostrá todos los múltiplos de 7 que hay entre a y b.

a = int(input("Ingrese el primer número (menor): "))
b = int(input("Ingrese el segundo número (mayor): "))

print(f"Múltiplos de 7 entre {a} y {b}:")
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)