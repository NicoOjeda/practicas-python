#Cuarto desafio python
#Alumno: Nicolas Ojeda
#Creado: 14/4  21:13

# Se necesita calcular el salario semanal de un trabajador de la construcción, dada la tarifa horaria y la cantidad de horas trabajadas diariamente.

tarifa_hora = float(input('ingrese la tarifa por hora: '))
cantidad_horas = float(input('ingrese la cantidad de horas trabajadas: '))

salario_semanal = (tarifa_hora * cantidad_horas)*5

print('El salario semanal es es:', salario_semanal)