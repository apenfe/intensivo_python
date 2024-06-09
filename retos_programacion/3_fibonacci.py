# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
# la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(numero=50):

    print(0)
    print(1)
    print(1)
    print(2)
    n_2 = 1
    n_1 = 2
    n=n_1+n_2

    for i in range(2,numero+1):

        print(n)
        n_2 = n_1
        n_1 = n
        n = n_1+n_2

fibonacci()