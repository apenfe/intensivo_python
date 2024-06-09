# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
# lo resuelvan automáticamente.

import re
def contar_palabras(frase):
    frase = frase.lower()
    contador_palabras = {}

    frase = frase.replace(",", "")
    frase = frase.replace(".", "")
    frase = frase.replace(";", "")

    palabras = re.split(r'\s', frase.strip())

    for palabra in palabras:

        if palabra not in contador_palabras:
            contador_palabras[palabra] = 1
        else:
            contador_palabras[palabra] += 1

    return contador_palabras

palabras = contar_palabras("hola a todos, gracias a todos")

for palabra, veces in palabras.items():
    print(f"palabra: {palabra}, veces: {veces}")