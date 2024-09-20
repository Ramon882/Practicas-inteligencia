toyota = ['yaris', 'corolla', 'camry', 'tacoma']  # Crea una lista con modelos de coches Toyota

cocheeliminado = toyota.pop(0)  # Elimina y almacena el elemento en el índice 0 (que es 'yaris') en la variable cocheeliminado

print(toyota)  # Imprime la lista después de eliminar el primer elemento, que ahora será ['corolla', 'camry', 'tacoma']

print('el coche eliminado es :' + cocheeliminado)  # Imprime el coche eliminado, que es 'yaris'
