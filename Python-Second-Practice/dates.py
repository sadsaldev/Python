# Dates

from datetime import datetime # Trabajar con fechas completas (año, mes, día, horas, minutos, segundos)

# Fecha ingresada manualmente
my_datetime = datetime(2024, 7, 21, 22, 30, 5)

print(my_datetime)
print(my_datetime.year) # Imprimir elementos específicos de la fecha ingresada
print(my_datetime.month)

# Imprimir fecha actual
now = datetime.now()
print(now)
print(now.day) # Imprimir elementos específicos de la fecha actual


from datetime import time # Trabajar solo con horas, minutod y segundos

my_time = time(3, 45)
print(my_time.minute) # Imprimir minutos especificados


from datetime import date # Trabajar solo con fechas de año, mes y dia

my_date = date.today() # Obtener fecha actual
print(my_date)
print(my_date.month) # Imprimir elementos específicos de la fecha actual


new_year = datetime(2025, 1, 26)
print(new_year - now) # Saber cuantos días faltan desde la fecha actual para llegar a la fecha establecida manualmente