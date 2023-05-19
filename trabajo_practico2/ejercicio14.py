# 14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
# múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
# ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
# no es bisiesto.

año= int(input('ingrese un año para comprobar si es bisiesto: '))

def bisiesto(año):
    if (año%4 == 0 and año%100!= 0):
        print(f'{año} es bisiesto')
    elif(año%400 ==0):
        print(f'{año} es bisiesto')
    else:
        print(f'{año} no es bisiesto')

bisiesto(año)

