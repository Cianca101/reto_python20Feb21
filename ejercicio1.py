### Ejercicio 1

def number_lenght(number):
    counter = 0 # Contador en ceros
    number_string = str(number)

    # Filtro tipo de dato y negativos
    if number.isdigit() and >= 0:
        for i in number_string:
            counter += 1
    else:
        return None, "Dato no Valido"

    return counter

number_lenght(12345)

