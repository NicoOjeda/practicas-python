# 4. Que dada la base y altura de un triángulo nos calcule su área.

base= float(input('Ingrese la base del triangulo: '))
altura= float(input('Ingrese la altura del triangulo: '))

def area_triangulo(base,altura):
    total= (base*altura)/2
    print(f'El area del triangulo es {total}')
    
area_triangulo(base,altura)