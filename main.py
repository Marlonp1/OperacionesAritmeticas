def encontrar_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Solicitar al usuario que ingrese los números, con validación de enteros positivos
numero1 = int(input("Ingrese el primer número entero positivo: "))
numero2 = int(input("Ingrese el segundo número entero positivo: "))
while numero1 <= 0 or numero2 <= 0:
    print("Ambos números deben ser enteros positivos.")
    numero1 = int(input("Ingrese el primer número entero positivo: "))
    numero2 = int(input("Ingrese el segundo número entero positivo: "))

# Calcular el MCD y mostrar el resultado
mcd = encontrar_mcd(numero1, numero2)
print("El máximo común divisor de", numero1, "y", numero2, "es:", mcd)

