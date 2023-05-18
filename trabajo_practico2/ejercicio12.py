# 12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
# mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

dia = input('ingrese un dia de la semana: ').lower()

def dias(dia):
    if (dia == 'lunes'):
        print(f'Hoy es {dia}, "Buena semana"')
    elif(dia == 'viernes'):
        print(f'Hoy es {dia}, ultimo dia de la semana')
    elif(dia == 'sabado' or dia == 'domingo'):
        print(f'Hoy es {dia}, "Buen fin de semana"')
    else:
        print(f'Hoy es {dia}, faltan algunos dias para el fin de semana')

dias(dia)
