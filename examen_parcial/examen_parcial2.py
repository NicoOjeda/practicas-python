# EJERCICIOS 2)
# Escribe una función llamada lista_decimal() que recibe una lista de números enteros y quita
# todos los elementos mayores que 9. Por último, la función debe retornar la lista ordenada.
# Salida esperada:
# ENTRADA = [4,9,10,20,5] SALIDA = [4,5,9]


numeros_enteros  = [4,9,10,20,5]
numeros_mayores=[]

def lista_decimal2(numeros_enteros):
    for i in numeros_enteros:
        if i<=9:
            numeros_mayores.append(i)
    print(sorted(numeros_mayores))

lista_decimal2(numeros_enteros)




# def lista_decimal(numeros_enteros):
#     for i in numeros_enteros:
#         if (i>9):
#             numeros_enteros.remove(i)
#     num= sorted(numeros_enteros)
#     print(num)
        
# lista_decimal(numeros_enteros)