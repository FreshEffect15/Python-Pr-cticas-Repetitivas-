#Implementá un menú que permita al usuario elegir entre:
#Sumar dos números
#Restar dos números
#Salir
#El menú debe repetirse hasta que el usuario elija salir. Validá las opciones.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

while True:
    print("Menú:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado de la suma es:", sumar(num1, num2))
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado de la resta es:", restar(num1, num2))
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")