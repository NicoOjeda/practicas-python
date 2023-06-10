# EJERCICIOS 2) Se tiene los siguientes datos del nivel del rio (en metros) en el puerto de concordia,
# para los últimos 5 días hábiles de la semana.
# Escribir un programa Python para permitir ingresar los datos por consola de los 5 días y
# guardarlos en una lista llamada altura_rio_puerto_concordia[].
# a. Mostrar la altura mínima semanal y en qué día de la semana ocurrió.
# b. Mostrar la altura máxima semanal y en que día de la semana ocurrió.
# c. Calcular el promedio del nivel en la semana.

altura_rio_puerto_concordia = []

def ingrese_altura():
    for i in range(0,5):
        alturas = float(input('Ingrese la altura de los dias de la semana: '))
        altura_rio_puerto_concordia.append(alturas)
    print(f'Alturas son {altura_rio_puerto_concordia}')


ingrese_altura()

def alt_max(altura_rio_puerto_concordia):
    altura_max = max(altura_rio_puerto_concordia)
    dia_semana = altura_rio_puerto_concordia.index(altura_max)
    match dia_semana:
        case 0:
            print(f'altura maxima semanal es {altura_max} el dia lunes')
        case 1:
            print(f'altura maxima semanal es {altura_max} el dia martes')
        case 2:
            print(f'altura maxima semanal es {altura_max} el dia miercoles')
        case 3:
            print(f'altura maxima semanal es {altura_max} el dia jueves')
        case 4:
            print(f'altura maxima semanal es {altura_max} el dia viernes')

alt_max(altura_rio_puerto_concordia)

def alt_min(altura_rio_puerto_concordia):
    altura_min = min(altura_rio_puerto_concordia)
    dia_semana = altura_rio_puerto_concordia.index(altura_min)
    match dia_semana:
        case 0:
            print(f'altura mínima semanal es {altura_min} el dia lunes')
        case 1:
            print(f'altura mínima semanal es {altura_min} el dia martes')
        case 2:
            print(f'altura mínima semanal es {altura_min} el dia miercoles')
        case 3:
            print(f'altura mínima semanal es {altura_min} el dia jueves')
        case 4:
            print(f'altura mínima semanal es {altura_min} el dia viernes')

alt_min(altura_rio_puerto_concordia)