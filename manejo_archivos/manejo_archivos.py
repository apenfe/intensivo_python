from urllib.request import urlopen
import json

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