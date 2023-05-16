# 3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
# cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

importe_sin_iva= float(input('Ingrese el importe sin IVA: '))
porcentaje_iva= input('Ingrese el porcentaje de IVA a aplicar: ')

def total_factura(importe,porcentaje):
    if porcentaje:
        porcentaje= int(porcentaje)
        agregado_iva= importe*(porcentaje/100)
        total= importe+agregado_iva
        print(f'el total de la factura es {total}')
    else:
        agregado_iva= importe*(21/100)
        total= importe+agregado_iva
        print(f'el total de la factura es {total}')
        
total_factura(importe_sin_iva,porcentaje_iva)