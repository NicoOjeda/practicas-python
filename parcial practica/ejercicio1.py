# EJERCICIO1) Escribir un programa Python que calcule el índice de masa corporal de una persona
# (IMC).
# Muestre por pantalla el estado en el que se encuentra esa persona en función del valor de IMC:
# Valor de IMC | Diagnóstico
# < 16 | Criterio de ingreso en hospital
# De 16 a 17 | Infrapeso
# De 17 a 18 | Bajo peso
# De 18 a 25 | Peso normal (saludable)
# De 25 a 30 | Sobrepeso (obesidad de grado I)
# De 30 a 35 | Sobrepeso crónico (obesidad de grado II)
# De 35 a 40 | Obesidad premórbida (obesidad de grado III)
# > 40 | Obesidad mórbida (obesidad de grado IV)


peso = float(input('Ingrese su peso en kilos (decimal separado por punto): '))
altura = float(input('Ingrese su altura en Metros (decimal separado por punto): '))

masa_corporal = round(peso/(altura**2),2)

print(f'Su masa corporal es {masa_corporal}')

def calcular_masa(masa_corporal):
    if masa_corporal < 16 :
        print("Tu estado es Criterio de ingreso en hospital")
    elif masa_corporal >= 16 and masa_corporal < 17: 
        print("Tu estado es Infrapeso")
    elif masa_corporal >= 17 and masa_corporal < 18: 
        print("Tu estado es Bajo peso")
    elif masa_corporal >= 18 and masa_corporal < 25: 
        print("Tu estado es Peso normal (saludable)")
    elif masa_corporal >= 25 and masa_corporal < 30: 
        print("Tu estado es Sobrepeso (obesidad de grado I)")
    elif masa_corporal >= 30 and masa_corporal < 35: 
        print("Tu estado es Sobrepeso crónico (obesidad de grado II)")
    elif masa_corporal >= 35 and masa_corporal < 40: 
        print("Tu estado es Obesidad premórbida (obesidad de grado III)")
    else:
        print("Tu estado es Obesidad mórbida (obesidad de grado IV)")

calcular_masa(masa_corporal)