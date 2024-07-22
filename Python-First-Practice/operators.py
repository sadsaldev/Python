# Operadores aritméticos

# Con números
print (6 + 3)
print (6 - 3)
print (6 * 3)
print (6 / 3)
print (6 % 3) # Devuelve el residuo de la división entre ambos números
print (6 ** 3) # Exponente, elevar 6 a la 3 en este caso
print (6 // 3) # En el caso de que una división sea inexacta y devuelva decimales, lo que hace el floor es quitarlos y devolver solo la parte entera

# Con strings
a = 6
print('Hola ' + 'Mundo') # Suma dos strings para imprimirlos juntos
print('Hola ' * 6) # Imprimirá el mensaje la cantidad de veces especificada
print('Hola ' + str(a)) # Para poder imprimir variables cuyo tipo de dato es diferente


# Operadores comparativos

print (4 < 8)
print (4 > 8)
print (4 == 8)
print (4 <= 8)
print (4 >= 8)
print (4 != 8)

print ('a' < 'b') # Devuelve true ya que "b" es mayor a "a" al estar más cerca de la z en el abecedario. Para la comparación de cadenas, la letra es mayor si está más cerca del final del abecedario
print ('a' > 'b') # Devuelve false ya que la "a" no puede ser mayor a la "b", la "b" está más cerca de la z, por ende es mayor


# Operadores lógicos

print (4 < 6 and 7 > 9 ) # and 
print (4 < 6 or 7 > 9) # or
print(not( 4 < 6)) # not -> Invierte el resultado de la expresión evaluada. En este caso 4 es menor que 6, por lo que debería devolver True, pero al aplicar Not, devolverá False en su lugar


print((not(7 != 7) and 6 > 5) and ('rozar' < 'rotar' or not(3 == 5)))