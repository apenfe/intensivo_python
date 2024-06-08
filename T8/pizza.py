def make_pizza(size,*toppings):
    print(f"\nhaciendo una pizza {size} con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")