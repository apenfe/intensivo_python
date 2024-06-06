pedidos_bocadillos = ['atun','pastrami','queso','lomo','pastrami','vegetal','pastrami']

bocadillos_terminados = []

print("No queda pastrami")

while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')

while pedidos_bocadillos:

    bocadillo_actual = pedidos_bocadillos.pop()
    print(f"Preparando bocadillo de {bocadillo_actual}")

    bocadillos_terminados.append(bocadillo_actual)

print(bocadillos_terminados)