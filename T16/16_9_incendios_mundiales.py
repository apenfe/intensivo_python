from pathlib import Path
import csv
import plotly.express as px

path= Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

brillos, longitudes, latitudes = [], [], []

for columna in reader:
    brillos.append(float(columna[2]))
    longitudes.append(float(columna[1]))
    latitudes.append(float(columna[0]))

title = "Incendios mundiales"
fig = px.scatter_geo(lat=latitudes,lon=longitudes, size=brillos, title=title,
                     color=brillos,color_continuous_scale='Viridis',labels={'color':'Magnitud incendio'},
                     projection='natural earth')
fig.show()