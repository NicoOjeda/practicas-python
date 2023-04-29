# Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al derecho que al revés. Por ejemplo: rayar, kayak, somos.

texto = input('Ingrese el texto a comprobar:')

texto_convertido = texto[::-1]

if(texto == texto_convertido):
    print('La palabra ingresada es palíndromo')
else:
    print('La palabra ingresada no es palíndromo')
