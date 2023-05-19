# 13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
# A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
# resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
# el grupo que le corresponde.

nombre = input('Ingrese su nombre: ').lower()
inicial= nombre[0]
sexo = input('Ingrese la letra de su sexo Femenino "f" o masculino "m": ').lower()

def grupos(inicial,sexo):
    if((inicial< "m" and sexo=="f") or (inicial> "n" and sexo=="m")):
        print('Tu grupo es el A')
    else:
        print('Tu grupo es el B')
        
grupos(inicial,sexo)