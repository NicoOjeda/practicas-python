# 6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
# de una lista vacía:

lista_vacia = []

# a. Agregar un elemento al final.
agregar_final = input('Ingrese un elemento al final de la lista: ')

def elemento_final(agregar_final,lista_vacia):
    lista_vacia.append(agregar_final)
    print(lista_vacia)

elemento_final(agregar_final,lista_vacia)

# b. Agregar un elemento al principio.
agregar_principio = input('Ingrese un elemento al principio de la lista: ')

def elemento_final(agregar_principio,lista_vacia):
    lista_vacia.insert(0, agregar_principio)
    print(lista_vacia)

elemento_final(agregar_principio,lista_vacia) 
print("----------------")

# c. Quitar un elemento al final.
# d. Quitar un elemento al principio.