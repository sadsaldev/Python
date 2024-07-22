def second_large():
    num_list = [13, 7, 9, 11, 8]
    num_list.sort(reverse = True)
    print(num_list[1])
    
second_large()

def time_conversor():
    
    askhoras = int(input("Ingrese las horas: "))
    askminutos = int(input("Ingrese los minutos: "))
    asksegundos = int(input("Ingrese los segundos: "))
    
    time_list = [askhoras, askminutos, asksegundos]
    
    print(time_list)
    
    horas = time_list[0] * 3600000
    minutos = time_list[1] * 60000
    segundos = time_list[2] * 1000
    
    resultado = (horas + minutos + segundos)
    
    print(f'La cantidad total en milisegundos de los valores ingresados (horas, minutos y segundos) es: {resultado}')

time_conversor()


def fizzbuzz():
    for numbers in range(1, 101): #Rango de 1 a 100
        
        if numbers %3==0 and numbers %5==0:
            print("fizzbuzz")
        elif numbers %3==0:
            print("fizz")
        elif numbers %5==0:
            print("buzz")
        else:
            print(numbers)
    
    # Para saber si un número es múltiplo de otro se utiliza el operador %. Esto determina si el número al ser divido por el número del cual
    # se quiere averiguar si es múltiplo o no, es igual a cero, es decir, la división es exacta.
        
fizzbuzz()

