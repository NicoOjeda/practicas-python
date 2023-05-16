# 1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

nombre= input('Ingrese nombre: ')

def saludo(nombre):
    print(f'¡Hola {nombre}!')
    
saludo(nombre)