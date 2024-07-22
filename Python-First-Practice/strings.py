# Strings

first_string = 'Arroz con huevo'
second_string = 'Café con leche'

# Buena práctica para concatenar
print(f'Esto es un texto de dos variables: {first_string}, {second_string}')

other_string = 'Hola'
a,b,c,d = other_string;

print(a);
print(b);
print(c);
print(d);

print(f'{a}{b}{c}{d}')

print(first_string.upper()) # Todo en uppercase
print(first_string.capitalize()) # Primera letra en mayúscula
print(first_string.lower()) # Todo en lowercase
print(len(first_string)) # Cuenta cantidad de caracteres
print(first_string.find('h')) # Devuelve la posición en la que está el caracter que especifiquemos
print(first_string.count('o')) # Cuenta la cantidad de veces que un caracter especificado está en la variable

print(first_string.upper().isupper())
print(first_string.lower().isupper())