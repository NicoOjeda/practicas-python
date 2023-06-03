# 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
# muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).

materias = ["Introduccion a la informatica", "Programacion1", "Diseño grafico", "arquitectura de computadoras", "Programacion2"]

def impresion(materias):
    for i in materias:
        print(i)
        
impresion(materias)