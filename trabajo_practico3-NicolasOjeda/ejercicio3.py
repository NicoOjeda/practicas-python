# 3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
# frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
# debajo la misma lista pero sólo con las frutas que añadió el usuario.

frutas = ["banana", "manzana", "pera"]
fruta_nueva = input("ingrese una fruta: ")
frutas.append(fruta_nueva)

def impresion_frutas(fruta_nueva,frutas):
    for i in range(0,2):
        fruta_nueva = input("ingrese una fruta: ")
        frutas.append(fruta_nueva)
    print(frutas)
    print(f'Las frutas ingresadas son: {frutas[3:len(frutas)]}')
    
impresion_frutas(fruta_nueva, frutas)
