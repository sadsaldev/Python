# Classes
# Para declarar clases es recomendable usar el camelCase
# Las clases en Python se utilizan para crear objetos que tienen propiedades y métodos (acciones).
class oneHuman:
    # El método __init__ es el inicializador (constructor) de la clase. Es llamado automáticamente cuando se crea una nueva instancia de la clase.
    def __init__(self, height, age, weight):
        # Human properties
        self.height = height
        self.age = age
        self.weight = weight
        # Self es una referencia al objeto actual (la instancia de la clase). Estas líneas asignan los valores de los parámetros a las propiedades del objeto
    
    # Human actions
    # Este es un método de la clase que representa una acción que puede realizar un objeto de esta clase. 
    def eat(self):
        print(f'El humano de {self.age} años está comiendo.')

# Crear una instancia de la clase oneHuman
# Esto crea un nueo objeto de la clase oneHuman llamado human_1 con una altura de 180cm, una edad de 23 años y un peso de 72kg
human_1 = oneHuman(180, 23, 72)

# Objeto: human_1 - Propiedades: height, age, weight - Acciones: eat

# Mostrar las propiedades del humano
print(f'El humano 1 mide {human_1.height}cm, pesa {human_1.weight}kg y tiene {human_1.age} años.')

# Llamar al método eat
human_1.eat()

# Esta clase define un "molde" para crear objetos con propiedades (altura, edad y peso) y un método (accion)
# Que puede realizar (eat). Luego, se crea un objeto de esta clase y se accede a sus propiedades y métodos