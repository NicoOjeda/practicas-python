# 4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
# realizar lo siguiente:

paises = ["Argentina","Brasil", "Bolivia","Paraguay","Venezuela"]

#a. Imprimir la cantidad de elementos que tiene la lista.
print(f'La cantidad de elementos de las lista son {len(paises)}')
print("----------------")

# b. Imprimir el primer y último elemento.
print(f'El primer elemento es {paises[0]} y el ultimo {paises[-1]} ')
print("----------------")

# c. Imprimir el resto.
print(f'El resto de elementos es {paises[1:4]} ')
print("----------------")

# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
# la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
pais = input('Ingrese un pais (No olvide la primera letra con mayuscula): ')

def esta_o_no(pais,paises):
    for i in paises:
        if (i == pais):
            return print(f'El indice de {pais} es: {paises.index(pais)}')
    else:
        print(f'{pais} no esta en la lista')

esta_o_no(pais,paises)
print("----------------")
# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
# la lista. Quitar el elemento correspondiente de esa posición.

indice = int(input('Ingrese un numero del 0 al 4 para borrar un pais de la lista: '))

def borrar_pais(indice):
    print(f'se elimino {paises[indice]} de la lista.' )
    del paises[indice]
    print(paises)

borrar_pais(indice)
print("----------------")
# f. Imprimir la lista en orden inverso.
paises.reverse()

print(f'Los paises en orden inverso son: {paises}')
print("----------------")

# g. Vaciar la lista.

paises.clear()

print(f'Se vacio la lista de paises: {paises}')