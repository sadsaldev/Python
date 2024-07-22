# Conditionals

num = 7
Lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '

if 4 > 6: 
    print('4 es menor que 6')
elif num != 7:
    print('La variable numero es igual a 7')
elif num > 9:
    print('La variable numero es menor que 9')
else: 
    print('No se cumplió ninguna condición')
    
    # Si al evaluar consecutivamente las condiciones y una resulta verdadera, ejecutará las acciones específicas para ese caso y no evaluará las siguientes
    
if len(Lorem) > 100 : 
    print('La cadena Lorem tiene más de 100 caracteres')
    
print('exit')