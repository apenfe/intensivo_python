cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# aqui viene la funcion reverse que cambia el orden del array, pero no en orden alfabetico, si no de indice

cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)

print(f"En total tengo {len(cars)} coches")