from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/eq_data_30_day_m1.json')
contenido= path.read_text()
all_eq_data = json.loads(contenido)

path = Path('eq_data/readable_eq_data.json')
contenido_legible = json.dumps(all_eq_data, indent=4)
path.write_text(contenido_legible)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

magnitudes, longitudes, latitudes = [], [], []

for diccionario in all_eq_dicts:
    magnitud = diccionario['properties']['mag']
    longitud = diccionario['geometry']['coordinates'][0]
    latitud = diccionario['geometry']['coordinates'][1]
    magnitudes.append(magnitud)
    longitudes.append(longitud)
    latitudes.append(latitud)

title = 'Terremotos globales'
fig = px.scatter_geo(lat=latitudes,lon=longitudes, size=magnitudes, title=title,
                     color=magnitudes,color_continuous_scale='Viridis',labels={'color':'Magnitud Ritchter'},
                     projection='natural earth')
fig.show()