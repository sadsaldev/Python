# Exceptions

try:
    print(5 + '3')
except NameError as error:
    print('Error de tipo NameError. Los tipos de datos no son compatibles:' , error)
except TypeError as error:
    print('Error de tipo TypeError. Los tipos de datos no son compatibles:', error)
else:
    print('Números sumados correctamente.') # Este else solo se ejecutará cuando lo que se ejecuta en el try no devuelve ningún error
finally:
    print('Fin de la operación') # Finally se ejecutará siempre sin importar si hubo un error en el try o no
    
