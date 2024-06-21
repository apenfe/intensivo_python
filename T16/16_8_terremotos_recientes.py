from pathlib import Path
import json
import plotly.express as px
from urllib.request import urlopen

path= Path('eq_data/16_8_data.json')

respuesta = urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson")
respuesta = respuesta.read()
all_eq_data = json.loads(respuesta)
contenido_legible = json.dumps(all_eq_data, indent=4)
path.write_text(contenido_legible)

all_eq_dicts = all_eq_data['features']

magnitudes, longitudes, latitudes, titulos = [], [], [], []

for diccionario in all_eq_dicts:
    magnitudes.append(diccionario['properties']['mag'])
    longitudes.append(diccionario['geometry']['coordinates'][0])
    latitudes.append(diccionario['geometry']['coordinates'][1])
    titulos.append(diccionario['properties']['title'])

title = str(all_eq_data['metadata']['title'])
fig = px.scatter_geo(lat=latitudes,lon=longitudes, size=magnitudes, title=title,
                     color=magnitudes,color_continuous_scale='Viridis',labels={'color':'Magnitud Ritchter'},
                     projection='natural earth',hover_name=titulos)
fig.show()