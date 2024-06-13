class Usuario:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def describir_usuario(self):
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellido)

    def saludar_usuario(self):
        print(f"Hola soy {self.nombre} {self.apellido}")

class Admin(Usuario):

    def __init__(self,nombre,apellido,privilegios):
        super().__init__(nombre,apellido)
        self.privilegios = privilegios

    def ver_privilegios(self):
        print(self.privilegios)

privilegios = ["ver cuantas","cambiar contraseña"]

admin = Admin("adrian","peñalver",privilegios)
admin.ver_privilegios()