from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import re

fichero = 'weather_data/death_valley_2018_simple.csv'
path = Path(fichero)
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

indice_min = 0
indice_max = 0

for indice, columna in enumerate(header_row):
    if columna == 'TMAX':
        indice_max=indice
    if columna == 'TMIN':
        indice_min = indice

dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high = int(row[indice_max])
        low = int(row[indice_min])
    except ValueError:
        print(f"Falta un dato para la fecha {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# trazar temperaturas maximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# dar formato al trazado

# Extract year from the filename
year_match = re.search(r'\d{4}', fichero)
year = year_match.group(0) if year_match else 'Año desconocido'

# Extract ciudad de filename
ciudad_match = re.search(r'/([^/]+?)_\d', fichero)
ciudad = ciudad_match.group(1).replace("_"," ") if ciudad_match else 'Lugar desconocido'

ax.set_title(f'Temperaturas maximas y minimas {year}, {ciudad}', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperaturas (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()