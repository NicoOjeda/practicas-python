# 7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
# con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
# usuario:

tareas_pendientes = ["lavar la ropa","ordenar el escritorio","pasear al perro"]
tareas_terminadas= []

# a. Agregar nuevas tareas pendientes.
tarea_p= input("Ingrese tarea pendiente: ").lower()

def pendientes(tarea_p):
    while tarea_p != "salir":
        tareas_pendientes.append(tarea_p)
        tarea_p= input('Ingrese otra tarea pendiente o "salir" para terminar: ').lower()
    print(tareas_pendientes)

pendientes(tarea_p)
print("----------------")

# b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
# de la lista de pendientes a la de terminadas.

tarea_t= input("Marque una tarea pendiente como terminada: ").lower()

def pendientes(tarea_t):
        while tarea_t != "salir":
            if tarea_t in tareas_pendientes:
                indice = tareas_pendientes.index(tarea_t)
                del tareas_pendientes[indice]
                tareas_terminadas.append(tarea_t)
                tarea_t= input('Marque otra tarea pendiente como terminada o ingrese "salir" para terminar: ').lower()
            else:
                print('Esa tarea no esta ingresada')
                tarea_t= input('Marque otra tarea pendiente como terminada o ingrese "salir" para terminar: ').lower()    
        print(f'Estas son las tareas terminadas {tareas_terminadas} y estas las tareas pendientes pendientes {tareas_pendientes}')

pendientes(tarea_t)