import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

x_values_5 = range(1,6)
y_values_5 = [x**3 for x in x_values_5]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,color ='red', s=10)
ax.scatter(x_values_5,y_values_5,color ='blue', s=10)

#establece el titulo y las etiquetas
ax.set_title('cubic numbers',fontsize=24)
ax.set_xlabel('Values',fontsize=14)
ax.set_ylabel('cubos del valor',fontsize=14)

# establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(labelsize=14)

# establece el rango para cada eje

ax.axis([0,150,0,3_500_000])
ax.ticklabel_format(style='plain')

plt.show()
