#Cuarto desafio python
#Alumno: Nicolas Ojeda
#Creado: 14/4  21:13

#Elaborar un algoritmo que permita ingresar el número de partidos Ganados, Perdidos y Empatados, por un equipo en el torneo apertura, se debe demostrar su puntaje total. (Teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos.)


ganados= int(input("Ingrese la cantidad de partidos ganados: "))
perdidos= int(input("Ingrese la cantidad de partidos perdidos: "))
empatados= int(input("Ingrese la cantidad de partidos empatados: "))


puntaje_total = (ganados*3)+(perdidos*0)+(empatados*1)
print('El puntaje total es:', puntaje_total)