def encontrar_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitar al usuario que ingrese los números, con validación de enteros positivos
while True:
    try:
        numero1 = int(input("Ingrese el primer número entero positivo: "))
        if numero1 <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        numero2 = int(input("Ingrese el segundo número entero positivo: "))
        if numero2 <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        break
    except ValueError as error:
        print(error)

# Calcular el MCD y mostrar el resultado
mcd = encontrar_mcd(numero1, numero2)
print("El máximo común divisor de", numero1, "y", numero2, "es:", mcd)
