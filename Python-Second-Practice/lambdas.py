# Lambdas

# Se pueden definir como "Funciones" cuya lógica se escribe en una misma línea
# Es una buena práctica usarlas en vez de las funciones cuando se necesita crear algo pequeño para mejor optimización de los recursos
my_lambda = lambda num1, num2: num1 + num2 * 2
print(my_lambda(5,4))

# También pueden usarse dentro de funciones
def def_lambdas(value):
    return lambda number: value + number

print(def_lambdas(5)(5))