#Pedí al usuario un número entero y mostrá cada uno de sus dígitos por separado, en orden inverso.

numero = int(input("Ingrese un número entero: "))

while numero > 0:
    digito = numero % 10
    print(digito)
    numero = numero // 10
