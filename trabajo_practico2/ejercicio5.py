# 5. Que dado tres números ingresados por el usuario nos devuelva el promedio.

valor1= float(input('Ingrese el primer valor: '))
valor2= float(input('Ingrese el segundo valor: '))
valor3= float(input('Ingrese el tercer valor: '))

def promedio(valor1,valor2,valor3):
    promedio= (valor1+valor2+valor3)/3
    print(f'El promedio de {valor1},{valor2} y {valor3} es {promedio}')
    
promedio(valor1,valor2,valor3)