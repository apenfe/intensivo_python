uno = input('Inserte el primer numero:')
dos = input('Inserte el segundo numero:')

suma = 0
try:
    suma = int(uno) + int(dos)
except Exception as e:
    print("inserte dos numeros")
else:
    print(suma)