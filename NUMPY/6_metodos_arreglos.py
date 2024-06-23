import numpy as np

vector = np.arange(5,20)
matriz = np.linspace(1,10,20).reshape((5,4))

print(vector)
print(matriz)

# metodos max, min, argmax, argmin

vector_maximo = vector.max()
vector_minimo = vector.min()

print(f"Vector: \n{vector}")
print(f'Valor maximo del vector: {vector_maximo}')
print(f'Valor minimo del vector: {vector_minimo}')

matriz_maximo = matriz.max()
matriz_minimo = matriz.min()

print(f"Matriz: \n{matriz}")
print(f'Valor maximo de la matriz: {matriz_maximo}')
print(f'Valor minimo de la matriz: {matriz_minimo}')

# calculo del maximo por filas
matriz_max_fil = matriz.max(axis=1)
matriz_min_fil = matriz.min(axis=1)

print(f"Matriz: \n{matriz}")
print(f'Valor maximo de cada fila: {matriz_max_fil}')
print(f'Valor minimo de cada fila: {matriz_min_fil}')

# calculo del minimo por columnas
matriz_max_col = matriz.max(axis=0)
matriz_min_col = matriz.min(axis=0)

print(f"Matriz: \n{matriz}")
print(f'Valor maximo de cada columna: {matriz_max_col}')
print(f'Valor minimo de cada columna: {matriz_min_col}')

# para hallar la posicion absoluta del valor maximo y minimo
vector_pos_max = vector.argmax()
vector_pos_min = vector.argmin()

print(f"Vector: \n{vector}")
print(f'Valor maximo del vector: {vector_maximo}, ubicado en la posicion {vector_pos_max}')
print(f'Valor minimo del vector: {vector_minimo}, ubicado en la posicion {vector_pos_min}')

# para el caso de la matriz, debemos difinir si busco la posicion global absoluta o bien
# por filas y columnas

m_pos_max = matriz.argmax()
m_pos_min = matriz.argmin()
m_pos_max_fils = matriz.argmax(axis=1) # posicion del maximo en cada fila
m_pos_min_cols = matriz.argmin(axis=0) # posicion del minimo en cada fila

print(f"Matriz: \n{matriz}")
print(f'Valor maximo global de la matriz: {matriz_maximo}, ubicado en la posicion {m_pos_max}')
print(f'Valor maximo global de la matriz: {matriz_minimo}, ubicado en la posicion {m_pos_min}')
print(f'Posicion de los maximos en cada fila: {m_pos_max_fils}')
print(f'Posicion de los minimos en cada columna: {m_pos_min_cols}')

# metodos mean, std, y sum

# suma de todos los elementos del vector y la matriz
print(f'\nsuma elementos del vector: {vector.sum()}')
print(f'suma elementos de la matriz: {matriz.sum()}')

# promedio y desviacion estandar
print(f'\npromedio por columnas de la matriz: {matriz.mean(axis=0)}')
print(f'desviacion estandar de las filas de la matriz: {matriz.std(axis=1)}')

# metodo squeeze y expand_dims

# se crea un arreglo con dimensiones reduandantes
matriz3D = np.array(([[[0,7],[9,2],[5,8]]]))
print(f'matriz: {matriz3D}')
print(f'Tamaño: {matriz3D.shape}')

matriz_sq = matriz3D.squeeze()

print(f'tamaño original: {matriz3D.shape}')
print(f'Tamaño matriz comprimida: {matriz_sq.shape}')
print(f'Matriz original: \n{matriz3D}')
print(f'Matriz comprimida: \n{matriz_sq}')

# tambien podemos expandir los arreglos

matriz_ex = np.expand_dims(matriz_sq,axis=(0,3))
print(f'\nDimensiones de matriz expandida: {matriz_ex.shape}')
print(f'\n{matriz_ex}')

