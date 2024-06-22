import numpy as np

arreglo = np.arange(5,15)
print(arreglo)

# operaciones aritmeticas entre arreglo y escalar
# sumar la misma cantidad a cada elemento del arreglo
arreglo_1 = arreglo + 2
print(arreglo_1)

arreglo_1 += 2 # con += sobreescribe sobre la misma variable
print(arreglo_1)

# se puede +, -, *, elevar, dividir

# Operaciones aritmeticas entre arreglos

arreglo_1 = np.linspace(3,5,10)
arreglo_2 = np.linspace(7,9,10)
arreglo_3 = np.linspace(10,15,12)

print(arreglo_1 * arreglo_2) # requisito: deben ser del mismo tamaño

matriz_1 = arreglo_1.reshape(5,2)
matriz_2 = arreglo_2.reshape(5,2)
matriz_multip = matriz_1 * matriz_2
print(f"Tañamo matriz resultante: {matriz_multip.shape}")

arreglo_int = np.arange(0,10)
arreglo_float = np.linspace(2,8,10)
arreglos_mult = arreglo_int * arreglo_float

print(f'dtype arreglo 1: {arreglo_int.dtype}')
print(f'dtype arreglo 2: {arreglo_float.dtype}')
print(f'dtype arreglo resultante: {arreglos_mult.dtype}')

# Operaciones logicas arreglo/arreglo o arreglo/escalar

arreglo = np.linspace(5,50,20)
print(arreglo)
print(arreglo>=25)

arreglo_2 = np.linspace(4,60,20)
print(arreglo_2)

print(arreglo_2 >= arreglo)
print(arreglo_2 == arreglo)
print(arreglo_2 != arreglo)