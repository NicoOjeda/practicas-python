# 8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad= int(input('Ingrese su edad: '))

def edad_usuario(edad):
    if(edad>=18):
        print('Usted es mayor de edad')
    else:
        print('Usted es menor de edad')

edad_usuario(edad)
