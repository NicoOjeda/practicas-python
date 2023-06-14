# EJERCICIOS 3)
# Dada la siguiente lista de países del mercosur:
# paises=[“argentina”,”uruguay”,”brasil”,”bolivia”,”paraguay”,”chile”]
# Escriba un programa Python que permita al usuario:


# a) Ingresar nuevos países a la lista.
paises=["argentina","uruguay","brasil","bolivia","paraguay","chile"]

ingreso_pais= input('ingrese un nuevo pais: ')

def ingreso(paises,ingreso_pais):
    
    while ingreso_pais != "salir":
            paises.append(ingreso_pais)
            ingreso_pais= input('ingrese un otro pais: ')
    
    print(f'Los paises con el ingreso son {paises}')

ingreso(paises,ingreso_pais)

print("------")
# b) Mostrar la cantidad de elementos de la lista.

total= len(paises)
print(f'La cantidad de paises es {total}')
print("------")
# c) Eliminar el primer y último elemento.

def eliminar(paises):
    del paises[0]
    del paises[-1]
    print(f'Los paises con el primer y ultimo elemento eliminados son {paises}')

eliminar(paises)
print("------")
# d) Mostrar la lista a la inversa.

def lista_inversa(paises):
    paises.reverse()
    print(f'Los elementos a la inversa son {paises}')

lista_inversa(paises)
print("------")

# e) Por último, vaciar la lista.
def vaciar_lista(paises):
    paises.clear()
    print(f'la lista eliminada es {paises}')

vaciar_lista(paises)




# paises=["argentina","uruguay","brasil","bolivia","paraguay","chile"]

# ingreso_pais= paises.append(input('ingrese un nuevo pais: '))

# def ingreso(paises):
#     print(f'Los paises con el ingreso son {paises}')

# ingreso(paises)