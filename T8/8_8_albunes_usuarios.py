def hacer_album(nombre,titulo,numero_canciones = None):
    album = {}
    album["nombre"]=nombre
    album["titulo"]=titulo

    if numero_canciones:
        album["numero"]=numero_canciones

    return album

albunes = []

while True:
    print("inserte datos, pulse q para salir...")
    artista = input("Inserte nombre artista: ")
    album = input("Inserte nombre del album: ")

    if artista == "q" or album == "q":
        break

    album = hacer_album(artista, album)
    albunes.append(album)

for album in albunes:
    print(album)