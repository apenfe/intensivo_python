import numpy as np

A = np.random.randn(5,4) # matriz con numeros aleatorios de 5x4
B = np.random.randn(5,4)

print(A)

# multiplicar elemento a elemento las matrices
C = np.multiply(A,B)
print(C)

# elevar cada elemento de una matriz
D = np.power(A,2)
print(D)

# valor absoluto de cada elemento de una matriz
E = np.abs(B)
print(E)

# Funciones del algebra lineal

# multiplicacion de matrices
matriz1 = np.random.randn(3,4)
matriz2 = np.random.randn(4,5)
matriz3 = np.matmul(matriz1,matriz2)

print(f'Matriz 1 de tamaño: {matriz1.shape}')
print(f'Matriz 2 de tamaño: {matriz2.shape}')
print(f'La matriz resultante: \n{matriz3}')
print(f'de tamaño: {matriz3.shape}')

# producto punto (o producto interno de vectores)

vector1 = np.linspace(5,10,4)
vector2 = np.linspace(15,20,4)
vector3 = np.dot(vector1,vector2)
print(f'Vector 1 de tamaño: {vector1.shape}')
print(f'Vector 2 de tamaño: {vector2.shape}')
print(f'Resultado del producto punto: {vector3}')

# norma de un vector
vector4 = np.arange(0,3) - 5
vector5 = np.linalg.norm(vector4) # norma o magnitud del vector
print(vector4)
print(vector5)

# funciones trigonometricas
A = np.random.randn(10,4)
cosenos = np.cos(A)
print(cosenos)
print(cosenos.shape)

# funciones floating
arreglo2D = np.array([[3.5,2.6,8.1],[9.4,2.2,14.3]])
print(arreglo2D)
print(np.isnan(arreglo2D))

# ahora accedo al indice 0,2 y lo modifico como NaN
arreglo2D[0,2]=np.nan
print(arreglo2D)
print(np.isnan(arreglo2D))

# Redondeos
print(f'CEIL: {np.ceil(arreglo2D)}')
print(f'FLOOR: {np.floor(arreglo2D)}')

