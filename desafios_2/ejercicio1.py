# Escribir un programa que pida al usuario ingresar por teclado:
#     1.precio de la tarifa por hora
#     2.cantidad de horas que permanecio el vehiculo
# con estos datos se debera calcular el importe y mostrar por pantalla el importe que debera abonar en la cochera.
precio_hora= float(input('Ingrese el precio por hora: '))
cantidad_horas= float(input('Ingrese la cantidad de horas que permanecio el vehiculo: '))

def calculas_importe(precio,cantidad):
    importe_abonar= precio*cantidad
    print('El importe en pesos que debera abonar es: ',importe_abonar)
    
calculas_importe(precio_hora,cantidad_horas)
    
