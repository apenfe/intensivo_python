# guarda la informacion sobre una pizza que se está pidiendo

pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}

# resumen del pedido
print(f"You ordered a {pizza['crust']} pizza! with the followings toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")