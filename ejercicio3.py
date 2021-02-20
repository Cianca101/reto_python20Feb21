### Ejercicio 3

# Factorial de un numero

#ex factorial(3) -> (3*2*1)

def factorial(num):
    resultado = 1
    if num >= 0 and isinstance(num, int):
        for i in range(num):
            resultado *= (i + 1)
        return resultado
    else:
        return None, "Dato no valido"

