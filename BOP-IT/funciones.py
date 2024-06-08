import random
from IPython.display import display, Audio


def seleccionar_estado():
    estado = random.choice(('gira', 'estira', 'bop-it'))
    return estado


def comando_voz(estado):
    sonido = Audio(filename='C:\\Users\\adria\\intensivo_python\\intensivo_python\\BOP-IT\\' + estado + '.wav',
                   autoplay=True)
    display(sonido, clear=True)


def interaccion_usuario(estado):
    tecla = input('')
    tecla = tecla.lower()
    succes = False

    if estado == 'bop-it' and tecla == 's':
        succes = True
    if estado == 'gira' and tecla == 'd':
        succes = True
    if estado == 'estira' and tecla == 'a':
        succes = True

    return succes