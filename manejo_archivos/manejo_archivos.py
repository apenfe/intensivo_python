from urllib.request import urlopen
from pathlib import Path
import json

path = Path('datos.json')

respuesta = urlopen("https://gbfs.citibikenyc.com/gbfs/en/station_status.json")
respuesta = respuesta.read()

# Para acceder como tal al contenido (es decir al archivo JSON) debemos
# usar el método "loads" de json, generando un diccionario en Python

json_data = json.loads(respuesta)

# Imprimamos detalles del diccionario obtenido
print(f'json_data - keys: {json_data.keys()}')
#print(json_data['data'])

# La información se encuentra en el key "stationBeanList", que es una lista
# de diccionarios
nestaciones = len(json_data['data']['stations'])
estaciones = json_data['data']['stations']
print(f'Cantidad de estaciones: {nestaciones}')
print('\nUn ejemplo de los datos de una estación:')
print(estaciones[0])

# creamos el fichero de texto

with open('bikesNY.txt', 'w') as archivo:
    # Crear encabezado
    archivo.write('NOMBRE EST., BIC. DISPONIBLES, DIR.\n')

    # Procesar cada registro (estación), extraer los campos e incluirla
    # en el .txt sólo si hay bicicletas disponibles
    for estacion in estaciones:
        nombre = estacion['station_id']
        nbicis = estacion['num_bikes_available']
        nbicis += estacion['num_ebikes_available']
        direcc = estacion['legacy_id']

        if nbicis != 0:
            archivo.write(f'{nombre}, {nbicis}, {direcc}\n')

# Definir formato de columnas:
# - {0:<35}: columna 0, alineado a la izquierda (<) y ancho de 35 caracteres
# - {1:>17}: columna 1, alineado a la derecha (>) y ancho de 17 caracteres
# - {2:>35}: columna 2, alineado a la derecha (>) y ancho de 35 caracteres
formato_cols = '{0:<35} {1:>17} {2:>35}'

with open('bikesNY_v2.txt', 'w') as archivo:
    # Crear encabezado
    archivo.write(formato_cols.format('NOMBRE EST.', 'BIC. DISPONIBLES', 'DIR.\n'))

    # Procesar cada registro (estación), extraer los campos e incluirla
    #  en el .txt sólo si hay bicicletas disponibles
    for estacion in estaciones:
        nombre = estacion['station_id']
        nbicis = estacion['num_bikes_available']
        nbicis += estacion['num_ebikes_available']
        direcc = estacion['legacy_id']

        if nbicis != 0:
            archivo.write(formato_cols.format(nombre, nbicis, direcc + '\n'))

import csv  # Módulo que hace parte de la librería estándar de Python

with open('bikesNY.csv', 'w') as archivo:
    writer = csv.writer(archivo)

    # Escribir encabezado: una lista
    encabezado = ['NOMBRE EST.', 'BIC. DISPONIBLES', 'DIR.']
    writer.writerow(encabezado)

    # Y escribir fila por fila
    for estacion in estaciones:
        # Parse item
        nombre = estacion['station_id']
        nbicis = estacion['num_bikes_available']
        nbicis += estacion['num_ebikes_available']
        direcc = estacion['legacy_id']

        if nbicis != 0:
            fila = [nombre, nbicis, direcc]
            writer.writerow(fila)