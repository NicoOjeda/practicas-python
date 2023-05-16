# 2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el
# resultado.

numero= int(input('Ingrese un número entero positivo:'))
potencia= int(input('Ingrese una potencia a elevar:'))

def numero_potencia(numero,potencia):
    resultado= numero**potencia
    print(f'El resultado de el numero {numero} elevado a {potencia} es {resultado}')
    
numero_potencia(numero, potencia)