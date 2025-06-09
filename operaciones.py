# operaciones.py

# Esta función eleva un número a una potencia y suma los dígitos del resultado
def suma_digitos_potencia(base, exponente):
    resultado = base ** exponente
    suma = 0
    for digito in str(resultado):
        suma += int(digito)
    return suma
