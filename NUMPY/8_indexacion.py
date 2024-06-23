import numpy as np

arreglo1D = np.array([5,27,43,2,4,87,9])

print(f'Arreglo 1D: {arreglo1D}')
print(f'primer elemento del arreglo: {arreglo1D[0]}')
print(f'ultimo elemento del arreglo: {arreglo1D[-1]}')

print(arreglo1D[1:5])
print(arreglo1D[0::2])

# indexacion y slicing sobre arreglos multidimensionales

arreglo2D = np.random.rand(4,3)
print(arreglo2D.shape)
print(arreglo2D)

# acceder al elemento fila 3 columna 2
print(arreglo2D[3,2])

# acceder a una fila completa de la matriz
print(f'arreglo 2d: \n{arreglo2D}')
print(f'Slicing fila 2: {arreglo2D[2]}')

# acceder a una columna completa de la matriz
print(f'arreglo 2d: \n{arreglo2D}')
print(f'Slicing columna 1: {arreglo2D[:,1]}')

# acceder a una porcion tanto en filas como en columnas
# sintaxis: [fila_inicio:fila_fin+1,col_inicio:columna_fin+1]
print(f'Arreglo 2D: \n{arreglo2D}')
print(f'Slicing filas 1 a 3, columnas 0 a 2: \n{arreglo2D[1:4,0:3]}')

# Para 3 o mas dimensiones se aplica la misma logica
arreglo3D = np.random.randn(4,3,2)

print(arreglo3D[3,2,1])

print(arreglo3D)
# quedarse con el segundo canal
print(arreglo3D[:,:,1])

