class Restaurante:

    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre_restaurante} y es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante está abierto")
