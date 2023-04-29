# Programe una aplicación de consola que pregunte el precio total de la cuenta, luego pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el número de comensales y mostrar cuánto debe pagar cada persona.

precio_total=float(input('¿Cuanto es el total de la cuenta? $'))
cantidad_comensales= float(input('¿Cuantos comensales hay?'))

pago_comensal= precio_total / cantidad_comensales

print('Cada persona debe pagar: $', pago_comensal)