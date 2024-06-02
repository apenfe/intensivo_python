players = ['Carlos','martina','miguel','florence','eli']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

# en este caso hace lo mismo pero utilizando los indices negativos, muestras los tres ultimos
print(players[-3:])

print("Aqui estan los primeros jugadores del equipo")
for player in players[:3]:
    print(player.title())