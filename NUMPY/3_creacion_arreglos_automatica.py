import numpy as np

a = np.zeros((4,2,3)) # crea arreglos 3D de ceros, filas, comumnas y canales
print(a)

print(f'Diemnsiones del arreglo: {a.ndim}')
print(f'Tamaño del arreglo: {a.shape}')
print(f'Núemro de elementos del arreglo: {a.size}\n')

b = np.ones(7,dtype = float) # en este caso un vector de unos tipo float
print(b)
print(f'Diemnsiones del arreglo: {b.ndim}')
print(f'Tipo de datos del arreglo: {b.dtype}\n')

c = np.full((5,2),12.0) # crea arreglos del tamaño deseado con valor deseado
print(c)

print(f'Diemnsiones del arreglo: {a.ndim}')
print(f'Tamaño del arreglo: {a.shape}')
print(f'Núemro de elementos del arreglo: {a.size}')
print(f'Tipo de datos del arreglo: {b.dtype}\n')

""" Creacion de arreglos con arange + el metodo reshape """

arreglo_1 = np.arange(10)
print(arreglo_1)

arreglo_2 = np.arange(2,15)
print(arreglo_2)

arreglo_3 = np.arange(3,10,2)
print(arreglo_3)

arreglo_4 = np.arange(2,101,2)
arreglo_5 = arreglo_4.reshape((5,10))
print(arreglo_4)
print(arreglo_5)

arreglo_6 = np.arange(2,101,2).reshape((5,10))
print(arreglo_6)

""" Creacion de arreglos con linspace + el metodo reshape """
arreglo_7 = np.linspace(0,10,100)
print('El arreglo: ')
print(arreglo_7)
print(f'Tamaño del arreglo: {arreglo_7.shape}\n')

arreglo_8 = np.linspace(0,10,20).reshape((5,4))
print(arreglo_8)