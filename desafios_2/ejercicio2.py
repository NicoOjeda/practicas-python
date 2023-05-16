# Escribir un programa que pida al usuario ingresar por teclado:
#     1.cantidad de personas adultas
#     2.cantidad de personas menores
#     3.cantidad de dias de estadia en el hotel
#     4.tarifa por noche de la habitacion
# Tenga en cuenta que cada adulto paga el 100% de la tarifa por noche, mientras que cada menor paga el 70%. Calcular el importe de la estadia que debera abonar al hotel y luego mostrarlo por pantalla.

personas_adultas= float(input('Ingresar cantidad de personas adultas: '))
personas_menores= float(input('Ingresar cantidad de personas menores: '))
cantidad_dias= float(input('Ingresar la cantidad de dias de estadia: '))
tarifa_noche= float(input('Ingresar la tarifa por noche de la habitacion: $'))

def importe_total(adulto,menor,cantidad_dias,tarifa_noche):
    tarifa_por_dia=(adulto*tarifa_noche)+(menor*(tarifa_noche*0.7))
    tarifa_total= tarifa_por_dia*cantidad_dias
    print(f'La tarifa total a abonar sera: ${tarifa_total}')
    
importe_total(personas_adultas,personas_menores,cantidad_dias,tarifa_noche)