from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2018_simple.csv')
path2 = Path('weather_data/sitka_weather_2018_simple.csv')
lines = path.read_text().splitlines()
lines2 = path2.read_text().splitlines()

reader = csv.reader(lines)
reader2 = csv.reader(lines2)

header_row = next(reader)
header_row_2 = next(reader2)
print(header_row)
print(header_row_2)

dates, valle, sitka = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high = int(row[4])
    except ValueError:
        print(f"Falta un dato para la fecha {current_date}")
    else:
        dates.append(current_date)
        valle.append(high)

for row in reader2:

    try:
        high = int(row[5])
    except ValueError:
        print(f"Falta un dato")
    else:
        sitka.append(high)

# trazar temperaturas maximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,valle,color='red',alpha=0.5)
ax.plot(dates,sitka,color='blue',alpha=0.5)
ax.fill_between(dates,valle,sitka,facecolor='blue',alpha=0.1)

# dar formato al trazado
ax.set_title('Temperaturas maximas y minimas 2018 Valle de la Muerte', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperaturas (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()