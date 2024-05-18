motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print (motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# desde 0

motos =[]
motos.append('ducati')
motos.append('honda')
motos.append('yamaha')

motos.insert(0,'tenere 700')

del motos[-1] # elimina un elemento de la lista, en este caso borro el ultimo elemento
print(motos)

moto_eliminada = motos.pop()
print(motos)
print(moto_eliminada)

print(f"la ultima moto eliminada es {moto_eliminada}")

primera_eliminada = motos.pop(0)
print(f"Mi actual moto es una {primera_eliminada}")

motos.remove('ducati')
print(motos)