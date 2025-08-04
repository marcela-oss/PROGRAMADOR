# Menú interactivo en Python

print("------MENU-------")
print("1 - Saber si es positivo o negativo")
print("2 - Saber si es par o impar")
print("3 - Saber si es primo o no")

op = int(input("Ingrese una opción: "))

if op == 1:
    n1 = int(input("Ingrese un número: "))
    if n1 > 0:
        print("El número es positivo")
    else:
        print("El número es negativo")

elif op == 2:
    n1 = int(input("Ingrese un número: "))
    if n1 % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

elif op == 3:
    n1 = int(input("Ingrese un número: "))
    cont = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            cont += 1
    if cont == 2:
        print("El número es primo")
    elif cont > 2:
        print("El número no es primo")
else:
    print("Opción inválida")