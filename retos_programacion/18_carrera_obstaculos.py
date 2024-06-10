# Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras "run" o "jump"
#      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#      - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

def carrera(acciones,pista):

    if len(acciones) != len(pista):
        return False

    salida = list(pista)

    for i in range(len(acciones)):

        accion = acciones[i]
        tramo = pista[i]

        if accion == "run" and tramo == '_':
            salida[i] = '_'
        elif accion == "run" and tramo == '|':
            salida[i] = '/'
        elif accion == "jump" and tramo == '|':
            salida[i] = '|'
        elif accion == "jump" and tramo == '_':
            salida[i] = 'x'

    print(salida)

    if '/' in salida or 'x' in salida:
        return False
    else:
        return True

if carrera(["run","run","run","jump","run"],"---|-"):
    print(True)
else:
    print(False)
