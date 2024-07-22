# Sets 

my_set = {'Python', 'JavaScript', 'PHP'}
print(type(my_set))

print(my_set)

# Los sets no tienen orden especifico y no aceptan elementos repetidos

my_set.add('C#') # Añadir elemento. Debe ser un elemento que aún no esté en el set para que de verdad se añada
print(my_set)


my_set_0 = {'Python', 'JavaScript', 'PHP'}
my_set.difference_update(my_set_0) # Identificar la diferencia entre ambos sets, en este caso C# ya que fue añadido después en my_set
print(my_set)