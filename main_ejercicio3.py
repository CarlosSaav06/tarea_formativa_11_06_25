# Importamos la funcion desde el archivo operaciones.py
from operaciones import suma_digitos_potencia

# Pedimos al usuario los datos
base = int(input("Ingrese un numero entero positivo: "))
exponente = int(input("Ingrese el exponente: "))

# Verificamos que sean positivos
if base < 0 or exponente < 0:
    print("Ambos numeros deben ser positivos.")
else:
    resultado = suma_digitos_potencia(base, exponente)
    print("La suma de los digitos de", base, "^", exponente, "es:", resultado)
