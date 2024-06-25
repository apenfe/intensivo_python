"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo
 y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y
  muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
  que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

PESO_PAYASO = 112
PESO_MUNECA = 75

n_payasos = int(input('Numero de payasos vendidos: '))
n_munecas = int(input('Numero de muñecas vendidas: '))

print(f'El peso del ultimo paquete es de {(PESO_MUNECA*n_munecas)+(PESO_PAYASO*n_payasos)} gramos')

