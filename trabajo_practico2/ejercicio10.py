# 10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
# a. Todos los números impares desde 1 hasta ese número separados por comas.
# b. La cuenta atrás desde ese número hasta cero separados por comas.
# c. Que indique si es primo o no.
# d. Por último, su factorial.

numero = int(input('Ingrese un numero entero positivo: '))

# a. Todos los números impares desde 1 hasta ese número separados por comas.
def numeros_impares(numero):
    print('Impares')
    for i in range(1,numero+1,1):
        if(i%2!=0):
            print(i,end=",")
            
numeros_impares(numero)
print('-')


# b. La cuenta atrás desde ese número hasta cero separados por comas.
def cuenta_atras(numero):
    print('cuenta atras')
    for b in range(numero,-1,-1):
        print(b, end=",")

cuenta_atras(numero)
print('-')

# c. Que indique si es primo o no.
def numero_primo(numero):
    print('Es primo o no')
    contador = 0
    for c in range(1,numero+1,1):
        if(numero%c ==0):
            contador += 1
            
    if(contador==2):
        print(f'{numero} es primo')
    else:
        print(f'{numero} no es primo')

numero_primo(numero)

# d. Por último, su factorial.
factorial = 1

for d in range(numero, 1,-1):
    factorial *= d

print(f'El factorial de {numero} es {factorial}')