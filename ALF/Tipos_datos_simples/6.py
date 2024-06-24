"""Escribir un programa que lea un entero positivo,
, introducido por el usuario y después muestre en pantalla la suma de
 todos los enteros desde 1 hasta n.  La suma de los n
 primeros enteros positivos puede ser calculada de la siguiente forma:"""

n = int(input("Inserte un numero: "))

print(f'La suma de 1 a {n} es:')
print((n*(n+1))/2)