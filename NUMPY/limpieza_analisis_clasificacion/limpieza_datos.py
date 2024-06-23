import numpy as np
import matplotlib.pyplot as plt

# cargar dataset
data = np.load('dataset.npy')
print(f'Estructura datos leidos: {data.shape}')

plt.scatter(data[:,0],data[:,1])
plt.xlabel('Edad')
plt.ylabel('Nivel de compras €')

plt.show()