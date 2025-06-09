#Calcular el factorial de un numero
def factorial(n):
    if n < 0:
        return "El numero debe ser no negativo"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un numero entero no negativo: "))
print(f"El factorial de {numero} es {factorial(numero)}")
