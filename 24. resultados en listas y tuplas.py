entrada = input('que marca de auto necesitas?\n')  # Solicita al usuario que ingrese una marca de auto

marca = ('toyota', 'ford', 'nissan')  # Define una tupla con las marcas disponibles

if entrada in marca:  # Verifica si la entrada del usuario está dentro de la tupla 'marca'
    print('si lo tenemos')  # Si la marca está en la tupla, imprime 'si lo tenemos'
else:
    print('no lo tenemos')  # Si la marca no está en la tupla, imprime 'no lo tenemos'
