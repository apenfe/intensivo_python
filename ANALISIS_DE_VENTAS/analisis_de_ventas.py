import csv

def extraer_columna(data,index):

    col = [fil[index] for fil in data]
    del col[0:2]
    col = [float(item) for item in col]
    return col

def extraer_fila(data,index):

    fil=data[index]
    fila = [fil[0]] +  [float(item) for item in fil[1:]]
    return fila

with open('ventas.csv') as f:
    reader = csv.reader(f)
    datos = [tuple(row) for row in reader]

meses = []
ventas_mensuales = []

for col in range(2,25,2):
    mes = datos[0][col]
    columna = extraer_columna(datos,col+1)

    ventas_mensuales.append(sum(columna))
    meses.append(mes)

for mes, ventas in zip(meses,ventas_mensuales):
    print(f"{mes} - Ventas: {ventas:.2f}")

max_ventas = max(ventas_mensuales)
idx_max = ventas_mensuales.index(max_ventas)
mes_max_ventas = meses[idx_max]
print(f"\nEl mes con mas ventas fue: {mes_max_ventas} (€{max_ventas:.2f})")

min_ventas = min(ventas_mensuales)
idx_min = ventas_mensuales.index(min_ventas)
mes_min_ventas = meses[idx_min]
print(f"El mes con menos ventas fue: {mes_min_ventas} (€{min_ventas:.2f})\n")

productos = []
prod_ventas = []

for fil in range(2,10):
    fila = extraer_fila(datos,fil)
    productos.append(fila[0])

    monto_ventas = []

    for col in range(2,25,2):
        monto_ventas.append(fila[col+1])

    prod_ventas.append(sum(monto_ventas))

for producto, prod_venta in zip(productos,prod_ventas):
    print(f"{producto} - Ventas: {prod_venta:.2f}")

ventas_y_prods = list(zip(prod_ventas,productos))
ventas_y_prods.sort(reverse=True)

print(f"\nLos tres productos mas vendidos son: ")
for item in ventas_y_prods[0:3]:
    print(f"{item[1]} - Ventas: {item[0]:.2f}")

with open('reporte.txt','w') as f:
    f.write('meses con mayores y menores ventas: \n')
    f.write('-'*50+'\n')
    f.write(f'  - Mes con mejores ventas: {mes_max_ventas} (${max_ventas:.2f})\n')
    f.write(f'  - Mes con peores ventas: {mes_min_ventas} (${min_ventas:.2f})\n')

    # Top-3 productos más vendidos
    f.write('\nProductos más vendidos en el año:\n')
    f.write('-' * 50 + '\n')
    for item in ventas_y_prods[0:3]:
        f.write(f'  - {item[1]} (${item[0]:.2f})\n')

f.close()