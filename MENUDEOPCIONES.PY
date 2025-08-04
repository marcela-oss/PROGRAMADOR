# Menú de opciones
print("Menú de opciones:")
print("1. Sumar dos números")
print("2. Restar dos números")
print("3. Multiplicar dos números")
print("4. Dividir dos números")
print("5. Salir")

# Leer opción del usuario
opcion = int(input("Elige una opción (1-5): "))

# Operaciones según la opción
if opcion == 1:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La suma de {a} y {b} es {a + b}")

elif opcion == 2:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La resta de {a} y {b} es {a - b}")

elif opcion == 3:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La multiplicación de {a} y {b} es {a * b}")

elif opcion == 4:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    if b != 0:
        print(f"La división de {a} y {b} es {a / b}")
    else:
        print("No se puede dividir por cero")

elif opcion == 5:
    print("Saliendo del programa...")

else:
    print("Opción no válida, intenta nuevamente")
