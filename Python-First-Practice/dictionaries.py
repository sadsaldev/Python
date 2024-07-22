# Dictionaries

my_dict = {
            'Nombre' : 'Salomé',
            'Apellido' : 'Londoño',
            'Apodo' : 'Sadsal'
          }

print(type(my_dict))
print(my_dict)

print(my_dict['Apodo']) # Obtiene el valor de una clave especificada
print(my_dict.keys()) # Obtiene las claves presentes en el diccionario (Nombre, Apellido, Apodo)
print(my_dict.values()) # Obtiene los valores asociados a las claves presentes en el diccionario (Salomé, Londoño, Sadsal)

# Los dicts se pueden convertir a listas, tuplas o sets

my_dict = list(my_dict)
print(my_dict)

my_dict = set(my_dict)
print(my_dict)

my_dict = tuple(my_dict)
print(my_dict)