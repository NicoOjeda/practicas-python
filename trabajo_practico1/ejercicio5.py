# Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente forma: “La respuesta es XX”.

numero1= float(input('Ingrese el primer numero:'))
numero2= float(input('Ingrese el segundo numero:'))
numero3= float(input('Ingrese el tercer numero:'))

resultado = (numero1 + numero2) * numero3

print('La respuesta es', resultado)
