# Comprehension

regular_list = [1,2,3,4,5,6,7]
print(regular_list)

def sum_number(number):
    number += 10
    return number

comprehension_list = [i for i in range(8)]
print(comprehension_list)

comprehension_list = [i * i for i in range(8)] # Multiplicar por el mismo número
print(comprehension_list)

comprehension_list = [sum_number(i) for i in range(8)] # llamar a la función creada para sumarle 10 a cada uno
print(comprehension_list)

def sum_string(string):
    string += '_'
    return string   

my_string = 'Hola mundo'
comprehension_list = [sum_string(i) for i in my_string] # Llamar a la función creada para agregarle low dash a cada caracter de la cadena
print(comprehension_list)