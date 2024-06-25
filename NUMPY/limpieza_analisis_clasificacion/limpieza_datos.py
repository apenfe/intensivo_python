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

""" Algoritmo k-means """
def escalar_datos(datos):
    # obtner maximos y minimos en cada columna
    maxs = np.max(datos,axis=0)
    mins = np.min(datos,axis=0)

    # escalar cada columna con base en su maximo/minimo correspondiente
    x_s = (datos[:,0] - mins[0]) / (maxs[0] - mins[0])
    y_s = (datos[:,1] - mins[1]) / (maxs[1] - mins[1])

    # conformar el nuevo set de datos
    datos_s = np.vstack((x_s,y_s)) # arreglo de 2 x nº datos
    datos_s = datos_s.transpose() # arreglo de nº datos x 2

    return maxs,mins,datos_s

maximos, minimos, data_s = escalar_datos(data_c)
print(f'Maximos originales: {maximos}')
print(f'Minimos originales: {minimos}')

plt.scatter(data_s[:,0],data_s[:,1])
plt.xlabel('Edad')
plt.ylabel('Nivel de compras €')
plt.show()

# Establcer los centroides iniciales
def inicializar_centroides(datos,k,seed=None):
    if seed:
        # ajustar semilla (Para reproductibilidad)
        np.random.seed(seed)
    # escoger tres filas aleatoriamente
    idx = np.random.choice(datos.shape[0],k,replace=False)

    # seleccionar las coordenadas correspondientes a estas filas
    centroides = datos[idx,:]

    return centroides

centroides = inicializar_centroides(data_s, 3, 100)
print(centroides)

# calcular las distancias entre los puntos y los centroides
def calcular_distancias(datos,centroides):
    k = centroides.shape[0] # cantidad de centroides
    N = datos.shape[0] # cantidad de datos (N=368)
    dists = np.zeros((N,k))

    # calcular la distancia euclidea entre cada centroide y cada punto del set
    for i, centroide in enumerate(centroides):
        dists[:,i] = np.linalg.norm(datos-centroide,axis=1)

    return dists

distancias = calcular_distancias(data_s, centroides)
print(f'tamaño del dataset: {data_s.shape}')
print(f'Tamaño del arreglo con las distancias: {distancias.shape}')
print(f'Ejemplo de una distancia (dato 5): {distancias[5]}')

def clasificar(dists):
    cat = np.argmin(dists,axis=1)
    return cat

y = clasificar(distancias)
idx = 7
print(f'Punto a clasificar: {data_s[idx,:]}')
print(f'Centroides: \n{centroides}')
print(f'Distancia punto-centroides: {distancias[idx,:]}')
print(f'Resultado clasificacion: {y[idx]}')

def actualizar_centroides(datos,cats):
    n_cats = cats.max()+1 # numero de categorias
    centroides = []

    for i in range(n_cats):
        # tomar datos correspondientes a cada categoria
        cluster = datos[cats==i,:]
        # calcular el centroide como el promedio de las coordenadas del cluster
        centroide = np.mean(cluster,axis=0)
        # almacenar el centroide obtenido
        centroides.append(centroide)
    # retornar los centroides en formato NumPy
    return np.asarray(centroides)

centroides_nuevos = actualizar_centroides(data_s, y)
print(f'Centoides iniciales: \n{centroides}')
print(f'Centroides nuevos: \n{centroides_nuevos}')

SEED = 150  # La semilla del generador aleatorio (reproducibilidad del algoritmo)
ctr_new = inicializar_centroides(data_s, 3, SEED)  # Inicializar 3 centroides
delta = 200  # Puede ser cualquier valor relativamente "alto"

while delta > 1e-3:
    # Calcular distancias de cada dato con respecto a cada centroide
    dists = calcular_distancias(data_s, ctr_new)

    # Clasificar cada dato
    y = clasificar(dists)

    # Actualizar centroides
    ctr_old = ctr_new
    ctr_new = actualizar_centroides(data_s, y)

    # Actualizar delta
    diff = ctr_old - ctr_new
    delta = np.mean(np.linalg.norm(diff))
    print(delta)

plt.scatter(data_s[:,0],data_s[:,1])
plt.xlabel('Edad')
plt.ylabel('Nivel de compras €')
plt.scatter(ctr_new[:,0],ctr_new[:,1])
plt.show()

""" Analisis exploratorio final """

# transformar los datos de edad (columna 0) y nivel de compra (columna 1) a la escala origianal
data_x = data_s[:,0]*(maximos[0]-minimos[0]) + minimos[0]
data_y = data_s[:,1]*(maximos[1]-minimos[1]) + minimos[1]
data_os = np.vstack((data_x,data_y)).transpose()
print(data_os)

# obtener las agrupaciones
cluster1 = data_os[y==0,:]
cluster2 = data_os[y==1,:]
cluster3 = data_os[y==2,:]

def caracterizar_segmento(cluster,title):
    # obtener minimos/maximos de edad y nivel compras
    mins = np.min(cluster,axis=0)
    maxs = np.max(cluster,axis=0)

    # imprimir info
    print('-'*30)
    print(f'Segmento: {title}')
    print(f'\t Rango de edades: {mins[0]:.0f}-{maxs[0]:.0f} años')
    print(f'\t Niveles de compra: {mins[1]:.0f}-{maxs[1]:.0f} €')

caracterizar_segmento(cluster1,'1')
caracterizar_segmento(cluster2,'2')
caracterizar_segmento(cluster3,'3')

plt.scatter(data_os[:,0],data_os[:,1],c=y)
plt.xlabel('Edad')
plt.ylabel('Niveles de compra (€)')

plt.show()
