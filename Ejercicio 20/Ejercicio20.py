#Permití ingresar números hasta que se escriba la palabra "fin". Guardá solo los números distintos (sin repeticiones) y mostralos ordenados de menor a mayor al finalizar.

numeros = set()

while True:
    entrada = input("Ingrese un número o 'fin' para terminar: ")
    if entrada.lower() == "fin":
        break
    try:
        numero = float(entrada)
        numeros.add(numero)
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'fin'.")

ordenados = sorted(numeros)
print("Números únicos ingresados (ordenados):", ordenados)