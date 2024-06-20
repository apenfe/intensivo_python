from die import Die
numero = 6
veces = 50000

# creo dado de 6 y 10 caras
die_1 = Die(numero)
die_2 = Die(10)

results = []

for roll_number in range(veces):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frecuencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+ 1)

for value in poss_results:
    frequencey = results.count(value)
    frecuencies.append(frequencey)

print(frecuencies)

import plotly.express as px

title = f"Resultado de lanzar dos dados de {numero} y 10 caras {veces} veces"
labels = {'x':'Resultado', 'y':'Frecuencia'}
fig = px.bar(x=poss_results, y=frecuencies, title=title, labels=labels)

# añade personalizaciones al grafico
fig.update_layout(xaxis_dtick=1)

fig.show()