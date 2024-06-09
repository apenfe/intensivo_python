# Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

def natural_a_morse(texto):

    texto = texto.lower()

    morse = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", " ": " "
    }

    salida = ""

    for letra in texto:
        salida += morse[letra]
        salida += " "
    return salida

def morse_a_natural(texto):

    morse = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i",
        ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
        "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", " ": " "
    }
    palabras = texto.split("  ")
    salida = ""

    for palabra in palabras:
        letras = palabra.split()  # Las letras están separadas por un espacio
        for letra in letras:
            if letra in morse:
                salida += morse[letra]
        salida += " "

    return salida

print("hola a todos en morse seria: ")
morse = natural_a_morse("hola a todos")
print(morse)

print("Traducido de nuevo a lenguaje natural seria: ")
natural = morse_a_natural(morse)
print(natural)