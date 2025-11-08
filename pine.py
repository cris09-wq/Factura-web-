class Auto:
    
    def _init_(self, marca, modelo, numero_pasajeros, kilometraje, tipo_auto, disponible):
        self.marca = marca
        self.modelo = modelo
        self.numero_pasajeros = numero_pasajeros
        self.kilometraje = kilometraje
        self.tipo_auto = tipo_auto
        self.disponible = disponible

    def actualizar_kilometraje(self):
        print("actualizacion")
    
    def cambiar_estado(self):
        print("disponibilidad")

    
auto1 = Auto('ford', '2005', '2', '5000', 'convertible', True)
print(auto1.disponible)
print(auto1.marca)
print(auto1.kilometraje)
print(auto1.modelo)
print(auto1.numero_pasajeros)