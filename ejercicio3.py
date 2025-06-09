#Calcular la suma de los dígitos de un número elevado a una potencia
# Esta función eleva un número a una potencia y suma los dígitos del resultado
def suma_digitos_potencia(base, exponente):
    resultado = base ** exponente  # Elevamos el numero
    suma = 0
    for digito in str(resultado):  # Convertimos el numero en cadena para recorrer los digitos
        suma += int(digito)        # Sumamos cada digito como entero
    return suma

# Se pide al usuario la base y el exponente
base = int(input("Ingrese un numero entero positivo: "))
exponente = int(input("Ingrese el exponente: "))

# Se verifica que ambos numeros sean validos
if base < 0 or exponente < 0:
    print("Ambos numeros deben ser positivos.")
else:
    print("La suma de los digitos de", base, "^", exponente, "es:", suma_digitos_potencia(base, exponente))
