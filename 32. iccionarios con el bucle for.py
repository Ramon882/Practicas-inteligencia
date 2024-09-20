auto1 = {  # Diccionario que contiene información del auto1
    'modelo': "fiesta",  # Modelo del auto
    'marca': 'ford',     # Marca del auto
    'precio': "32000"    # Precio del auto
}
auto2 = {  # Diccionario que contiene información del auto2
    'modelo': "yaris",   # Modelo del auto
    'marca': "toyota",   # Marca del auto
    'precio': "52000"    # Precio del auto
}

# Itera a través de los elementos (clave-valor) del diccionario auto1
for x, y in auto2.items():  
    print(x, ':', y, '$')  # Imprime la clave (x) seguida del valor (y) y agrega el símbolo $
