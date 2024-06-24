import numpy as np
import matplotlib.pyplot as plt

# cargar dataset
data = np.load('dataset.npy')
print(f'Estructura datos leidos: {data.shape}')

plt.scatter(data[:,0],data[:,1])
plt.xlabel('Edad')
plt.ylabel('Nivel de compras €')

plt.show()

# Tras visualizar datos, debe de ver si existen valores nan, u otros valores
# para hacer una limpieza adecuada

# Primero vemos si esxiste algun NaN, si existen entonces ya analizamos to el set

if np.isnan(data).any():
    print()
    print(f'Faltan datos...')

    if np.isnan(data[:,0]).any(): # analizamos la columna 1 completa (Edad) X
        print(f'En la primera columna')

    if np.isnan(data[:,1]).any(): # analizamos la columna 2 completa (Gasto) Y
        print(f'En la segunda columna')

# En esta caso faltan datos y realizaremos la imputación por interpolacion
ind_nan = np.argwhere(np.isnan(data[:,1])) # estos son los indices de las posiciones a interpolar, es decir son NaN
ind_notnan = np.argwhere(~np.isnan(data[:,1])) # estos son los indices de donde hay cantidades numericas
print()
print(f'Faltan {ind_nan.shape} valores')
print(f'Tenemos {ind_notnan.shape} valores')

# Variables independientes (x = edad) y dependiente (y = nivel gasto) con los datos conocidos
x = data[ind_notnan,0] # vector de 369 x 1
x = x.flatten() # arreglo de 369 (requerido por la funcion de interpolacion)

y = data[ind_notnan,1].flatten()

# Los datos deben estar organizados de forma ascendente pero se debe preservar la relacion entre las columnas
# 1º obtendremos los indices que organizarias "x" (edad) de manera ascendente
idx_x = np.argsort(x)
print(x[idx_x]) # esta expresion es como un for, imprime tod el vector x con los nuevos indices

# 2º con estos indices se pueden organizar los vectores x e y
x = x[idx_x]
y = y[idx_x]

# Ahora ya se realiza la interpolacion de la libreria de NumPy
x_interp = data[ind_nan,0].flatten() # valores de edad donde se realizara la interpolacion, estos son los conocidos, cuyos gastos se desconocen
y_interp = np.interp(x_interp,x,y)

print(f'Valores de X (edad) interpolados: {x_interp}')
print(f'Valores de y (gasto) interpolados: {y_interp}')

# ahora ya se reemplazan los valores interpolados en las posiciones correspondientes del set
data[ind_nan,1]=y_interp.reshape(4,1)

# volvemos a verificar que no queda ningun NaN
print(np.isnan(data[:,0]).any())
print(np.isnan(data[:,1]).any())

""" ----- Manejo de Outliers ----- """

plt.scatter(data[:,0],data[:,1])
plt.xlabel('Edad')
plt.ylabel('Nivel de compras €')
plt.show()

# limpieza de edades: las filas con edades negativas o "muy grandes" se eliminan
mask_edad = (data[:,0] > 0) & (data[:,0] < 100)
data_c = data[mask_edad]
print(data.shape)
print(data_c.shape)

# limpieza de niveles compra: las filas con niveles negativos o superiores a 5000 se eliminan
mask_compra = (data_c[:,1] > 0) & (data_c[:,1] < 5000)
data_c = data_c[mask_compra]
print(data_c.shape)

plt.scatter(data_c[:,0],data_c[:,1])
plt.xlabel('Edad')
plt.ylabel('Nivel de compras €')
plt.show()

