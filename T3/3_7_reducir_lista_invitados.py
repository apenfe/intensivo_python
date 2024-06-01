personajes = ['cristobal colon']
personajes.append('Juan Carlos')
print(f"como fue el descubimiento de america, {personajes[0]}?")
print(f"como se vive en EAU, {personajes[1]}?")
print()

personajes.insert(0,'juan')
personajes.insert(2,'luis')
personajes.insert(-1,'paco')

print(f"Invitado a la cena, {personajes[0]}")
print(f"Invitado a la cena, {personajes[1]}")
print(f"Invitado a la cena, {personajes[2]}")
print(f"Invitado a la cena, {personajes[3]}")
print(f"Invitado a la cena, {personajes[4]}")
print()

print(f"Solo puedo invitar a dos personas")

eliminado = personajes.pop(0)
print(f"{eliminado}, la cena queda cancelada")

eliminado = personajes.pop(1)
print(f"{eliminado}, la cena queda cancelada")

eliminado = personajes.pop(2)
print(f"{eliminado}, la cena queda cancelada")

del personajes[0] # elimina un elemento de la lista, en este caso borro el ultimo elemento
del personajes[1] # elimina un elemento de la lista, en este caso borro el ultimo elemento

print(personajes)