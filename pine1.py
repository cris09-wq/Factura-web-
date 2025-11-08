class Carrito:
    pass
carro1 = Carrito()
print(carro1)

class Carro:
    def __init__(self,marca,modelo,color):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        
carro1 = Carro("bmw","rc","blanco")
print(type(carro1))
print(carro1)
print("El carro es: ",carro1.marca, " ",carro1.modelo, " ",carro1.color)