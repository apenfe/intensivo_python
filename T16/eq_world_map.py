from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/eq_data_30_day_m1.json')
contenido= path.read_text()
all_eq_data = json.loads(contenido)

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