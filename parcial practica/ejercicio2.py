# EJERCICIO 2) Para convertir entre las diferentes escalas de temperaturas Celsius (ºC), Fahrenheit
# (ºF) se realizan los siguientes cálculos:
# • De ºC a ºF: se multiplica por 1,8 y se suma 32.
# • De ºF a ºC: se resta 32 y se divide entre 1,8.
# Escribir un programa Python con dos funciones para permitir la conversión de escalas:
# convertir_celsius_fharenhait()
# convertir_fharenhait_celsius()
# Mostrar la conversión de 53C°
# Mostrar la conversión de 77F° 

temperatura_celsius = 53
temperatura_farenheit = 77

def convertir_celsius_fharenhait(temp):
    celsius_fharenhait = temp*1.8+32
    print(f'La conversion de {temp} grados celsius a farenheit es {celsius_fharenhait}')

convertir_celsius_fharenhait(temperatura_celsius)

def convertir_fharenhait_celsius(temp):
    fharenhait_celsius = (temp-32)/1.8
    print(f'La conversion de {temp} grados farenheit a celsius es {fharenhait_celsius}')

convertir_fharenhait_celsius(temperatura_farenheit)
