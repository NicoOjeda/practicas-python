# Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el día, mes y año. Ej: Usuario ingresa: 17/05/1985 Programa imprime: Día: 17, Mes: 05 y Año: 1985

fecha = input('Ingrese una fecha en este formato dd/mm/aaaa: ')

dia= fecha[0:2]
mes= fecha[3:5]
año= fecha[6:10]

print(f'La fecha ingresada es el Dia: {dia}, Mes: {mes} y Año: {año}')