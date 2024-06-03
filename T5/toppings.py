requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"añadiendo {requested_topping}")
else:
    print("No hay ningun ingrdiente que añadir")