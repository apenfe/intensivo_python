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

