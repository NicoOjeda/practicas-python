# 11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
# encuentran en dicha frase.

frase = input('Ingrese una frase: ')

def cantidad_vocales(frase):
    contador= 0
    for i in frase:
        match i:
            case 'a':
                contador +=1
            case 'e':
                contador +=1
            case 'i':
                contador +=1
            case 'o':
                contador +=1
            case 'u':
                contador +=1
    print(f'La cantidad de vocales en la frase es: {contador}')


cantidad_vocales(frase)
