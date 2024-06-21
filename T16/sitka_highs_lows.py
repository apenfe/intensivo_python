from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    high = int(row[5])
    low = int(row[6])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# trazar temperaturas maximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')

# dar formato al trazado
ax.set_title('Temperaturas maximas y minimas 2018', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperaturas (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()