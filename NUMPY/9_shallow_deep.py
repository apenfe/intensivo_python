import numpy as np

# copias shawoll o poco profundas

arr = np.array([5,27,82,3,14,5])
print(arr)

slc = arr[3:]
print(slc)

slc[1]= -10
print(slc)
print(arr)

# al hacer slicing el nuevo arreglo queda ligado al arreglo anterior, debo desacoplar
# debo usar una copia deep, profunda

slc2 = arr[3:].copy()
print(slc2)

slc2[2] = -200
print(slc2)

print(arr)