class Restaurante:

    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    def describir_restaurante(self):
        print(f"El restaurante se llama {self.nombre_restaurante} y es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante está abierto")

    def establecer_numero_servido(self,num):
        self.numero_servido = num

    def incrementar_numero_servido(self,num):
        self.numero_servido += num


restaurante = Restaurante("Muelle 12", "Copas")
print(f"Numero de clientes servidos {restaurante.numero_servido}")
restaurante.numero_servido = 4
print(f"Numero de clientes servidos {restaurante.numero_servido}")
restaurante.establecer_numero_servido(8)
print(f"Numero de clientes servidos {restaurante.numero_servido}")
restaurante.incrementar_numero_servido(4)
print(f"Numero de clientes servidos {restaurante.numero_servido}")
