# 5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
# usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
# de los números ingresados por el usuario deberá ser almacenado en una lista. A
# continuación, realice las siguientes tareas:


numeros = input('Ingrese números enteros y la palabra "fin" para terminar: ')
lista=[]

def impresion(numeros):
    while numeros != "fin":
        lista.append(int(numeros))
        numeros = input('Ingrese números enteros y la palabra "fin" para terminar: ')
    print(f'Los numeros ingresados son : {lista}')

impresion(numeros)
print("----------------")

# a. Determinar el máximo.
def maximo(lista):
    max = lista[0]
    for i in lista:
        if i> max:
            max = i
    print(f'El numero maximo es: {max}')

maximo(lista)
print("----------------")

# # b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
lista.sort()
print(f'El segundo valor maximo de la lista es {lista[-2]}')
print("----------------")

# c. Determinar el mínimo.
def minimo(lista):
    min = lista[0]
    for i in lista:
        if i< min:
            min = i
    print(f'El numero minimo es: {min}')

minimo(lista)
print("----------------")

# d. Calcular la multiplicación de todos los números de la lista.
def multiplicar(lista):
    multiplicado = 1
    for i in lista:
        multiplicado *= i
    print(f'La multiplicacion de todos los numeros es : {multiplicado}')

multiplicar(lista)
print("----------------")

# e. Contar los valores pares e impares.
pares = 0
impares = 0

def pares_impares(pares,impares):
    for i in lista:
        if(i%2 == 0):
            pares +=1
        else:
            impares+=1
    print(f'Los numeros pares son: {pares}')
    print(f'Los numeros impares son: {impares}')
    
pares_impares(pares,impares)
print("----------------")

# f. Remover los elementos repetidos.

def repetidos(lista):
        sin_repetir=[]
        for x in  lista:
            if x not in sin_repetir:
                sin_repetir.append(x)
        print(f'La lista sin elementos repetidos es {sin_repetir}')
    
repetidos(lista)