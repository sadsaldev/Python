# Loop

numero = 0
while numero < 10: 
    numero += 1 # Esto indica que se añadirá una unidad a la variable numero por cada iteración que se haga, hasta que llegue a 10 y se detenga el bucle
    print(numero)
    if numero < 5:
        print('Es menor que 5')
    elif numero == 5:
        print('Es igual que 5')
    elif numero > 5:
        print('Es mayor que 5')

print('While loop ended')

#Ejemplo de for para imprimir los elementos de una lista
my_list = [76, 43, 4.5, 3, 24]
for number in my_list: # Por cada número de la lista, imprima al número
    print(number)
print('For list loop ended')
    
# Ejemplo de for con range para que un elemento se imprima cierta cantidad de veces
for x in range (51):
    print(x)
    if x == 25:
        print('Llegó a 25')
        break
print('For range loop ended')

