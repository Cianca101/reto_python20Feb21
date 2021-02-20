### Ejercicio 4

#Funcion formatear numeros
#ex format(1000) --> '1,000'
# format(43214124) --> '43,214,124'

def format(number):
    str_num = str(number)   #convertir number a str
    rev_num = list(str_num) #convertir str a list
    rev_num.reverse() #invevrtir lista
    new_number = 0
    for i in len(rev_num):
        if (i+1) % 3 == 0:
            rev_num[i].append(',')
        else:
            pass
        rev_num.reverse()
        new_number = str(rev_num)
        formated_number = int(new_number)
    return new_number

