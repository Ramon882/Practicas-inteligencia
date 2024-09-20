def carro(modelo, marca, *args):  # Nombres de los parámetros sin comillas
    print('El modelo del auto es:', modelo)  # Imprime el modelo del auto
    print('La marca del auto es:', marca)    # Imprime la marca del auto
    for x in args:  # Itera sobre los argumentos adicionales
        print('Año de fabricación:', x)  # Imprime cada argumento adicional
        
lista = [2010, 2220, 2410]  # Lista de años de fabricación
carro('yaris', 'toyota', *lista)  # Llamada a la función con argumentos correctos
