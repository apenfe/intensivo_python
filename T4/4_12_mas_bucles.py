my_foods = ['pizza','falafel','kebab']

friend_foods = my_foods[:]

my_foods.append('carne')

print("Mis comidas favoritas son:")

for food in my_foods:
    print(food)

print("\nLas comidas favoritas de mis amigos son:")

for food in friend_foods:
    print(food)