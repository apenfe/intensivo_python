alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['points']=10

print(f"Acabas de ganar {alien_0['points']} puntos")
print (alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_1 = {}

alien_1['color']='blue'
alien_1['points']=5
print(alien_1)

# cambio de color
alien_1['color']='amarillo'
print(alien_1)

alien_2 = {'x_position':0, 'y_position':25,'speed':'medium'}
print(f"Posicion original {alien_2['x_position']}")

# se mueve al alien hacia la derecha basandos e en velocidad actual

if alien_2['speed'] == 'low':
    x_position = 1
elif alien_2['speed'] == 'medium':
    x_position=2
else:
    x_position=3

alien_2['x_position']+=x_position
print(f"Posicion actual {alien_2['x_position']}")

# eliminar pares clave-valor
print(alien_2)
del alien_2['x_position']
print(alien_2)