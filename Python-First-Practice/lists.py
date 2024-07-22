# Listas

my_list = ['Python', 53, False, 74, 'Pan']
print(type(my_list))
print(my_list)
# print(my_list[4])

my_list.append(53) # Agregar elemento a la lista al final
print(my_list)

my_list.insert(3, 'Café') # Agregar elemento a la lista especificando la posición donde quiere que se agregue
print(my_list)

my_list.remove('Pan') # Quitar elemento de la lista
print(my_list)

print(my_list.pop(2)) # Quitar el elemento ubicado en la posición especificada, en este caso sería el False. Y al encerrarlo en un print, nos devolverá el elemento que borró
print(my_list)

print(my_list.count(53)) # Cuenta la cantidad de veces que un elemento está presente en la lista

my_list.reverse() # Coloca la lista al revés
print(my_list)

my_list.clear() # Limpia la lista y la deja vacía
print(my_list)