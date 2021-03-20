### Ejercicio 1

def number_lenght(number):
    counter = 0 # Contador en ceros
    # Filtro tipo de dato y negativos
    if number >= 0 and isinstance(number, int):
        number_string = str(number)
        for i in number_string:
            counter += 1
    else:
        return None, "Dato no Valido"
    return counter






# Array Inicial
arrayColor = [
  'rojo',
  'azul',
  'amarillo',
  'verde',
  'rojo',
  'amarillo',
  'rojo'
]

# Se desea obtener los indices que se repiten, el resultado es: [4, 5, 6]
versus = [ ]    # array de comparación
counter = [ ]   # array para guardar indice de repetidos
n = 0   # contador de iteración
for i in arrayColor:    # recorrer el array inicial
    if i not in versus: # busca el elemento i de arrayColor en versus, si NO lo encuentra
        versus.append(i)    # inserta elemento i en versus
        n += 1  # aumenta el contador de iteración
    else:   # si SI lo encuentra
        n += 1  # contador de iteración
        counter.append(n-1) # inserta el valor actual de la iteración

