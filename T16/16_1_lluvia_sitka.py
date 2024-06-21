from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates, rain = [], []

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        r = float(row[3])
    except ValueError:
        print(f"Falta un dato para la fecha {current_date}")
    else:
        dates.append(current_date)
        rain.append(r)

# trazar lluvia
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,rain,color='red',alpha=0.5)

# dar formato al trazado
ax.set_title('Lluvia 2018 Sitka', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('lluvia', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()