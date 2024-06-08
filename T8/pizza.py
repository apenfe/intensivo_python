def make_pizza(*toppings):
    print(f"\nhaciendo una pizza con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('champiñones','green peppers','extra cheese')

def make_pizza(size,*toppings):
    print(f"\nhaciendo una pizza {size} con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('grande','pepperoni')
make_pizza('grande','champiñones','green peppers','extra cheese')