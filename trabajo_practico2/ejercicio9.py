# 9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
# en que ambos números son iguales.

numero1= float(input('Ingrese un numero: '))
numero2= float(input('Ingrese otro numero: '))

def comparar(numero1,numero2):
    if(numero1>numero2):
        print(f'{numero2} es menor a {numero1}')
    elif(numero1<numero2):
        print(f'{numero1} es menor a {numero2}')
    else:
        print(f'{numero2} y {numero1} son iguales')

comparar(numero1,numero2)
