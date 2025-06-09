# Convertir un numero decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

# Se pide al usuario un numero entero positivo
numero = int(input("Ingrese un numero entero positivo: "))

# Se verifica que el número sea valido
if numero < 0:
    print("El numero debe ser positivo.")
else:
    print("El numero", numero, "en binario es", decimal_a_binario(numero))
