my_foods = ['pizza','falafel','kebab']

friend_foods = my_foods[:]

# si hacemos lo siguiente seria decir que son la misma direccion de memoria
# friend_foods=my_foods

my_foods.append('carne')

print("Mis comidas favoritas son:")
print(my_foods)

print("\nLas comidas favoritas de mis amigos son:")
print(friend_foods)