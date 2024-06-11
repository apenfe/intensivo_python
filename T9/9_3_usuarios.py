class Usuario:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def describir_usuario(self):
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellido)

    def saludar_usuario(self):
        print(f"Hola soy {self.nombre} {self.apellido}")

yo = Usuario("Adrián","Peñalver")
yo.describir_usuario()
yo.saludar_usuario()