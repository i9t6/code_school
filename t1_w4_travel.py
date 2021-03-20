#!/home/paco/ubuntu/py3/bin/python
print(f'Tareas para el viaje')
var_lista_tareas = []
n = 0
while n <= 4:
    var_lista_tareas.append(input(f"Tarea {n+1} : "))
    n += 1

var_recordar = int(input(f"Cual quieres recordar : ")) - 1
print(f'tienes que : {var_lista_tareas[var_recordar]}')

var_tarea_nueva = input(f'Tarea nueva :')
var_tarea_nueva_index = int(input(f'En que lugar :')) - 1
print(f'Pasar al baño \
\n\nlista completa')

var_lista_tareas.insert(var_tarea_nueva_index,var_tarea_nueva)
var_lista_tareas.append("pasar al baño")

print(f'La lista incluye : {var_lista_tareas} \
\n quitando la 1 y 2 nos queda : {var_lista_tareas[2:]}')




