def hacer_album(nombre,titulo,numero_canciones = None):
    album = {}
    album["nombre"]=nombre
    album["titulo"]=titulo

    if numero_canciones:
        album["numero"]=numero_canciones

    return album

print(hacer_album("Silvio rodriguez","habana",8))