# 15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
# validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
# informarle que no se puede procesar el dato.

letra = input('Ingrese una letra: ').lower()

def vocal(letra):
    if (len(letra) == 1):
            match letra:
                case 'a':
                    print(f'{letra} es vocal')
                case 'e':
                    print(f'{letra} es vocal')
                case 'i':
                    print(f'{letra} es vocal')
                case 'o':
                    print(f'{letra} es vocal')
                case 'u':
                    print(f'{letra} es vocal')
                case _:
                    print(f'{letra} no es vocal')
    else:
        print('Ingresaste mas de un caracter, no se puede procesar dato')

vocal(letra)

