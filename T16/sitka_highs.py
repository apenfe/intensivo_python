from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

# extraer temperaturas maximas

highs = []

for row in reader:
    high = int(row[5])
    highs.append(high)

# trazar temperaturas maximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs,color='red')

# dar formato al trazado
ax.set_title('Temperaturas maximas diarias, julio 2018', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperaturas (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()