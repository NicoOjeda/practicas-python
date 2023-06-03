# 2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
# Imprimir por pantalla el resultado.

numero = int(input("ingrese un numero: "))
orden=[]
orden.append(numero)

def numeros_ordenados(orden):
    for i in range(0,4):
        numero = int(input("ingrese un numero: "))
        orden.append(numero)
    orden.sort()
    print(orden)
numeros_ordenados(orden)