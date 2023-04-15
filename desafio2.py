#Segundo desafio python
#Alumno: Nicolas Ojeda
#Creado: 14/4  21:08

#Se desea calcular la distancia recorrida (m) por una lancha que tiene velocidad constante (m/s) durante un tiempo T (Sg).

velocidad = float(input("Ingrese la velocidad constante de la lancha en m/s:"))
tiempo= float(input("Ingrese el tiempo en segundos:"))

distancia_recorrida = velocidad * tiempo 

print('La distancia_recorrida por la lancha es:', distancia_recorrida, 'metros' )