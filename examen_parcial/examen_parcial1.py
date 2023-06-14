# EJERCICIOS 1)
# Escribir un programa que tome tres números enteros ingresados por el usuario y que imprima
# por pantalla el resultado de la suma y de la multiplicación de los mismos.


num1= int(input('Ingrese el primer numero: '))
num2= int(input('Ingrese el segundo numero: '))
num3= int(input('Ingrese el tercer numero: '))

def suma(num1,num2,num3):
    sumados = num1 + num2 + num3
    multiplicados= num1 * num2 * num3
    print("------")
    print(f'La suma de los numeros  {num1}, {num2} y {num3} es {sumados}')
    print("------")
    print(f'La multiplicacion de los numeros  {num1}, {num2} y {num3} es {multiplicados}')
    
suma(num1,num2,num3)