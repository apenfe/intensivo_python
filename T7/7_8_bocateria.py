pedidos_bocadillos = ['atun','queso','lomo']

bocadillos_terminados = []

while pedidos_bocadillos:

    bocadillo_actual = pedidos_bocadillos.pop()
    print(f"Preparando bocadillo de {bocadillo_actual}")

    bocadillos_terminados.append(bocadillo_actual)

print(bocadillos_terminados)