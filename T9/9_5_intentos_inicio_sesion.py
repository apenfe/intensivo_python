class Usuario:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_inicio_sesion = 0

    def describir_usuario(self):
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellido)

    def saludar_usuario(self):
        print(f"Hola soy {self.nombre} {self.apellido}")

    def incrementar_intento_inicio(self):
        self.intentos_inicio_sesion += 1

    def reset_intento_inicio(self):
        self.intentos_inicio_sesion = 0

yo = Usuario("Adrián","Peñalver")
yo.describir_usuario()
yo.saludar_usuario()
yo.incrementar_intento_inicio()
yo.incrementar_intento_inicio()
yo.incrementar_intento_inicio()
print(f"Intentos de inicio: {yo.intentos_inicio_sesion}")
yo.reset_intento_inicio()
print(f"Intentos de inicio: {yo.intentos_inicio_sesion}")