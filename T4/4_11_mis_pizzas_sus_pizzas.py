pizzas = ['cuatro quesos','barbacoa','carbonara']

pizzas_amigos = pizzas[:]

pizzas.append('5 quesos')
pizzas_amigos.append('piña')

print("Mis pizzas favoritas son: ")
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}")

print(f"\nLas pizzas de mis amigos son:")
for pizza in pizzas_amigos:
    print(f"Me gusta la pizza de {pizza}")