# 6. Que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra= input('Ingrese una palabra: ')

def imprimir(palabra):
    for i in range(0,10):
        print(palabra)
        
imprimir(palabra)