# Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y segundos son esos números de días.

dias = int(input('Ingrese numero de dias a calcular: '))

horas_calculadas = 24 * dias
minutos_calculados = (24*60)* dias
segundos_calculados = (24*60*60)* dias

print(f'Los dias ingresados equivalen a {horas_calculadas} horas, {minutos_calculados} minutos y {segundos_calculados} segundos')