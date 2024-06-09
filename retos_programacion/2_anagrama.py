# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

def anagrama(palabra_1,palabra_2):

    anagram = ''.join(reversed(palabra_1))

    # cadena_inversa = cadena[::-1] --> es el operador de slicing que se compone de tres partes: inicio:fin:paso

    # for caracter in range(len(cadena) - 1, -1, -1):
    #     cadena_inversa += cadena[caracter]
    # range(start, stop, step) acepta tres argumentos:
    # start: El valor inicial de la secuencia.
    # stop: El valor en el que la secuencia se detiene (no inclusive).
    # step: El paso o incremento entre cada número de la secuencia. Puede ser negativo para contar hacia atrás.

    if anagram == palabra_2:
        return True
    else:
        return False

print(anagrama("ramo","omar"))