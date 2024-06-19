def formato(ciudad,pais,habitantes=0):

    if habitantes != 0:
        texto = f"La ciudad de {ciudad.title()} es la capital de {pais.title()}, tiene {habitantes} habitantes."
        return texto
    else:
        texto = f"La ciudad de {ciudad.title()} es la capital de {pais.title()}"
        return texto