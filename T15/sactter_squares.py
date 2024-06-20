import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,color ='red', s=10)
# ax.scatter(x_values,y_values,c =(0,0.8,0), s=10)

#establece el titulo y las etiquetas
ax.set_title('Square numbers',fontsize=24)
ax.set_xlabel('Values',fontsize=14)
ax.set_ylabel('Cuadrado del valor',fontsize=14)

# establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(labelsize=14)

# establece el rango para cada eje

ax.axis([0,1100,0,1100000])
ax.ticklabel_format(style='plain')

plt.show()