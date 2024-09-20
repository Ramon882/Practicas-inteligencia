print('tiendita\n'
      'que deseas comprar?\n'
      '1. coca\n'
      '2. papas\n'
      '3. paleta\n'
      '4. donas\n')

comprar = [1, 2]  # Lista de artículos que el usuario desea comprar
dinero = 120  # Cantidad de dinero disponible
co = 20  # Precio de coca
pa = 40  # Precio de papas
pal = 15  # Precio de paleta
do = 20  # Precio de donas

# Verifica si el usuario desea comprar algo que no está especificado
if 0 in comprar:
    print('especifique una opción válida')

# Resta el costo de los artículos comprados del dinero disponible
if 1 in comprar:
    dinero -= co
if 2 in comprar:
    dinero -= pa
if 3 in comprar:
    dinero -= pal
if 4 in comprar:
    dinero -= do

# Verifica si el dinero es suficiente
if dinero <= 0:
    print('ya no te ajusta')
else:
    # Imprime el dinero restante solo si hay suficiente
    print('te quedan ' + str(dinero) + ' pesos')
