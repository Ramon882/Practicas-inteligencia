edad = int(input('que edad tienes?'))  # Solicita al usuario que ingrese su edad y la convierte en un número entero

if edad <= 0:  # Verifica si la edad es menor o igual a 0, lo cual no es válido
    print('error')  # Imprime 'error' si la edad es menor o igual a 0
elif edad >= 1 and edad <= 17:  # Verifica si la edad está entre 1 y 17
    print('estas chavo')  # Imprime 'estas chavo' si la edad está entre 1 y 17
elif edad <= 100:  # Verifica si la edad es menor o igual a 100
    print('estas viejo')  # Imprime 'estas viejo' si la edad está entre 18 y 100
else:
    print('error')  # Imprime 'error' si la edad es mayor a 100
