import numpy as np
import timeit

N = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7] # DIFERENTES TAMAÑOS DE LOS ARREGLOS Y LISTAS

for n in N:

    x_python = list(range(n))
    x_numpy = np.arange(n)

    t_python = timeit.timeit('sum(x_python)',"from __main__ import x_python", number = 1000)/1000
    t_numpy = timeit.timeit('x_numpy.sum()', "from __main__ import x_numpy", number=1000) / 1000

    print('-'*50)
    print(f'N = {n}')
    print(f'Tiempo de computo promedio en Python: {t_python} segundos')
    print(f'Tiempo de computo promedio en NumPy: {t_numpy} segundos')
    print(f'NumPy es {t_python/t_numpy:.1f} veces más rápido')


