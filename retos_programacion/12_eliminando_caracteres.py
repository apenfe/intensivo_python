# Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def eliminar_caracteres(cadena_1,cadena_2):

    out_1, out_2 = "",""

    for caracter in cadena_1:
        if caracter not in cadena_2:
            out_1+=caracter

    for caracter in cadena_2:
        if caracter not in cadena_1:
            out_2+=caracter

    return out_1, out_2

out1, out2 = eliminar_caracteres("bienvenidos","aeioudc")
print(out1)
print(out2)