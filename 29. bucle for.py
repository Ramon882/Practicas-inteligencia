colores = ['azul', 'negro', 'blanco', 'rojo']  # Crea una lista con varios colores

for x in colores:  # Recorre cada elemento en la lista colores
    if x == 'negro':  # Si el color actual es 'negro'
        continue  # Omite el resto del código en este ciclo y pasa al siguiente color
    print(x)  # Imprime el color actual si no es 'negro'
