personajes = ['cristobal colon']

personajes.append('Blas de lezo')

print(f"como fue el descubimiento de america, {personajes[0]}?")
print(f"como fue el asedio a Cartagena de indias, {personajes[1]}?")
print()

no_viene = personajes.pop(1)
print(f"{no_viene} no podra venir")

personajes.append('Juan Carlos')
print(f"como fue el descubimiento de america, {personajes[0]}?")
print(f"como se vive en EAU, {personajes[1]}?")
print()