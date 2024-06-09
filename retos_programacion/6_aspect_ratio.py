# Crea un programa que se encargue de calcular el aspect ratio de una
# imagen a partir de una url.
# - Url de ejemplo: https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

import requests
from PIL import Image
from io import BytesIO

# URL de la imagen
url = "https://i.blogs.es/0ca9a6/aa/1366_2000.jpeg"

# Descargar la imagen
response = requests.get(url)

if response.status_code == 200:
    # Cargar la imagen en PIL
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen
    img.show()

    widht, height = img.size
    aspect_ratio = widht / height
    # Mostrar la relación de aspecto
    print(f"Ancho: {widht}, Alto: {height}, Relación de aspecto: {aspect_ratio:.2f}")

else:
    print("Error al descargar la imagen")