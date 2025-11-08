class Carro:
    
    tipo_vehiculo = 'Terrestre'
    
    def __init__(self,marca,modelo,color):
        
        print("Generando carro: ",marca,modelo,color)
        
        
        self.marca= marca
        self.modelo= modelo
        self.color= color
        
    def acelerar(self):
        print("runnnrunnn")
        
    def tanquear(self, valor):
        print(f"Tanqueando {valor} peso")
        
print(Carro.tipo_vehiculo)
carro1 = Carro("bmw",", rc",", blanco")
print(type(carro1))
print(carro1.marca)
print(carro1.tipo_vehiculo)
carro1.acelerar()
carro1.tanquear(10000)

