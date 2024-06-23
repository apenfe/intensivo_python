import numpy as np

# concatenacion de arreglos
v1 = np.linspace(0,10,5)
v2 = np.linspace(30,40,5)
print(v1)
print(v2)
print()

# Para aplilarlos horizontalmente
v1v2_h = np.hstack((v1,v2))
print(v1v2_h)
print(v1v2_h.shape)
print()

# Para aplilarlos verticalmente, (deben tener mismo tamaño)
v1v2_v = np.vstack((v1,v2))
print(v1v2_v)
print(v1v2_v.shape)
print()

# Para apilar arreglos multidimensionales es igual
# si los apilo en horizontal, las mismas columnas, si es en vertical, filas

M1 = np.random.rand(2,3)
M2 = np.random.rand(2,3)

# apilar horizontal
Mh=np.hstack((M1,M2))
print(f'Matrices originales de tamaño: {M1.shape} y {M2.shape}')
print(f'Matriz resultante: \n{Mh}')
print(f'de tamaño: {Mh.shape}')
print()
# apilar verticial
Mv = np.vstack((M1,M2))
print(f'Matrices originales de tamaño: {M1.shape} y {M2.shape}')
print(f'Matriz resultante: \n{Mv}')
print(f'de tamaño: {Mv.shape}')
print()

# Si los arreglos no son del mismo tamaño, se puede usar concatenate
arr1 = np.array([[3,9,8],[4,23,2]])
arr2 = np.array([[12,24,5]])
print(arr1.shape)
print(arr2.shape)
print()

arr_filas = np.concatenate((arr1,arr2),axis=0) # concatenando por filas
print(arr_filas)
print(arr_filas.shape)
print()

# La funcion WHERE

arr = np.random.randn(2,3)
print(arr)

indices = np.where(arr<=0.5)
print(indices)
print()
resultado = arr[np.where(arr<=0.5)]
print(resultado)
print()

# otra forma d euso, es reemplazar los valores que sean coincidencias
resultado = np.where(arr<=0.5,np.nan,arr) # (condicion, valor si es true, valor si es false)
print(arr)
print(resultado)
print()

# Finalmente la funcion np.random.seed

print(np.random.randint(100)) # siempre un numero diferente

np.random.seed(23)
numero = np.random.randint(100) # en este caso, cada vez se dara el mismo numero aleatorio
print(numero)
print()

np.random.seed(100)
print(np.random.rand(2,2))
