# Escribe una función que reciba un texto y retorne verdadero o
# falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee
# de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

def palindrono(texto):

    texto = texto.lower()
    texto = texto.replace(" ","")
    texto = texto.replace(".","")
    texto = texto.replace(",", "")

    texto2 = texto[::-1]

    if(texto2 == texto):
        return True
    else:
        return False

print(palindrono("Ana lleva al oso la avellana."))

