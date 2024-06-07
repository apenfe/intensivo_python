# 1. Introducir saldo inicial
# 2. Introducir tasa de interés mensual
# 3. ciclo "while" sobre las ganancias:
#    3.1 Actualizar el mes, el saldo y las ganancias
#    3.2 Imprimir mensaje en cada iteración
# 4. Imprimir mensaje final

# 1. Introducir saldo inicial
saldo_inicial = float(input('Introduzca el monto inicial a invertir: '))

# 2. Introducir tasa de interés mensual
tasa_interes = input('Introduzca la tasa de interés mensual (ejemplo: 0.8%): ')

# 2a. Reajustar el str "tasa_interes"
tasa_interes = tasa_interes.replace("%", "")
tasa_interes = float(tasa_interes)

# 3. While
#  3a. Inicializar ganancias y mes
saldo = saldo_inicial
mes = 0
ganancias = saldo - saldo_inicial

while ganancias < saldo_inicial:
    # 3.1. Actualizar mes, saldo y ganancias
    mes += 1
    saldo += saldo * tasa_interes / 100
    ganancias = saldo - saldo_inicial

    # 3.2. Imprimir el mensaje indicando mes y saldo
    print(f'Mes: {mes}. Saldo: {saldo:.1f}')
# 4. Imprimir el mensaje final
print(f'Se requieren {mes} meses para que las ganancias sean iguales al monto inicial')