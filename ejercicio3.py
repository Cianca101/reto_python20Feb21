### Ejercicio 3

# Factorial de un numero

#ex factorial(3) -> (3*2*1)

def factorial(num):
    resultado = 1
    for i in range(num):
        resultado *= (i + 1)
    return resultado

