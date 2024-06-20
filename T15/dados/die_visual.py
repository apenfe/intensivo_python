from die import Die
numero = 6
veces = 1000

die = Die(numero)

results = []

for roll_number in range(veces):
    result = die.roll()
    results.append(result)

frecuencies = []

poss_results = range(1, die.num_sides + 1)

for value in poss_results:
    frequencey = results.count(value)
    frecuencies.append(frequencey)

print(frecuencies)

import plotly.express as px

title = f"Resultar de lanzar un dado de {numero} caras {veces} veces"
labels = {'x':'Resultado', 'y':'Frecuencia'}
fig = px.bar(x=poss_results, y=frecuencies, title=title, labels=labels)
fig.show()