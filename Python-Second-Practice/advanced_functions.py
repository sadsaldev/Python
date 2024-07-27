# Superior Order Functions -> Cuando se LLAMA una función dentro de otra función
def add_value(num):
    return num + 5

def add_value_2(num):
    return num + 10

def sum_values(num1, num2, f):
    return f(num1 + num2)
print(sum_values(7, 8, add_value)) # Llamamos a la otra función en cuestión
print(sum_values(7, 8, add_value_2)) 


# Closures -> Cuando se CREA una función dentro de otra función
def closure_number(original_num):
    def closure_new(num):
        return num + original_num
    return closure_new

my_fn = closure_number(3) # 3 en este caso es el original_num de closure_number
print(my_fn(2)) # 2 en este caso es el num de closure_new


# Map puede servir para ejecutar una misma función para cada elemento de una lista
# En este caso, dividirá por dos (que es la tarea que la función division_number se encarga de hacer) cada elemento de la lista list_numbers
list_numbers = [7, 10, 15, 25]
def division_number(number):
    return number / 2
request = list(map(division_number, list_numbers))
print(request)

# Forma optimizada con lambda para hacer la operación directa sin llamar a otra función
request = list(map(lambda number: number / 2, list_numbers))
print(request)


# Filter: necesita una función y un iterable, para filtrar sus elementos según los criterios dados
def filter_number(number):
    return number > 10
request = list(filter(filter_number, list_numbers))
print(request) # Output: [15, 25] -> Filtrará los números de la lista que son mayores a 10. Retorna solo lo verdadero

# Forma optimizada con lambda
request = list(filter(lambda number: number > 10, list_numbers))
print(request)

