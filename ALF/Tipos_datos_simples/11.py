"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
 Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
 final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada
  en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
  la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""

monto = float(input("Ingrese el valor de la cantidad a invertir: "))
interes = 4 / 100
anos = 3

for ano in range(anos):
    ganancia = monto * interes
    monto = monto + ganancia
    print(f'Año {ano+1}, monto: {monto} €')
