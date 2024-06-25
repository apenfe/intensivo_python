"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión."""

monto = float(input("Ingrese el valor de la cantidad a invertir: "))
interes = float(input("Ingrese el % de interes anual: "))
interes = interes / 100
anos = int(input('Ingrese el numero de años: '))

for ano in range(anos):
    ganancia = monto * interes
    monto = monto + ganancia
    print(f'Año {ano+1}, monto: {monto} €')

