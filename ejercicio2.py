### Ejercicio 2

# funcion recibe 2 argumentos (num y long), devolver lista
# con multiplos dada la longitud

# ex (7, 5)
# [7, 14, 21, 28, 35]

# [nx1, nx2, nx3, hasta index i]

lista_mult = []

def multiplos(num, leng):
    mult = 1

    if num >= 0 and leng >= 0 and isinstance(num, int) and isinstance(leng, int):
        for i in range(leng):
          lista_mult.append(f'{num}x{i+1}={num*i+1}')
    else:
        return None, "Dato no Valido"
    return lista_mult

