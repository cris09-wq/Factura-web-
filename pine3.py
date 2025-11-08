class Marvel:
    
    def __init__(self,Nombre,Fuerza,Pasado):
        
        print("Atribitos: ",Nombre,Fuerza,Pasado)
        
        self.Nombre = Nombre
        self.Fuerza = Fuerza
        self.Pasado = Pasado
        
    def Proteger_a_la_humanidad(self):
        print("Proteger a la humanidad")
        
    tipo_de_heroe = "Los vengadores"
            
print(Marvel.tipo_de_heroe)
personaje = Marvel("Iron man",", Mullonario",", Tragico")
print(type(personaje))
print("nombre:",personaje.Nombre)
personaje.Proteger_a_la_humanidad()

print("----------------------------------------- // ----------------------------------")

class Marvel_Villanos:
    
    def __init__(self,Villano,Poder,Pasado):
        print("Atributos: ",Villano,Poder,Pasado)
        
        self.Villano = Villano
        self.Poder = Poder
        self.Pasado = Pasado
        
    def derrotar_a_los_heroes(self):
        print("derrotar a los heroes")
        
    tipo_de_villano = "Multiverso de spider-man"
    
print(Marvel_Villanos.tipo_de_villano)    
Villano1 = Marvel_Villanos("Octpus",", Garras mecanicas",", Obsesión")
print(type(Villano1))
print("Nombre: ",Villano1.Villano)
Villano1.derrotar_a_los_heroes()

print("------------------------------------ // ---------------------------")
          
                    
class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def obtener_nota_promedio(self):
        return (self.nota1 + self.nota2) / 2

    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Nombre: {self.nombre}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Promedio: {promedio:.2f}")


# Prueba de la clase
estudiante1 = Estudiante("Carlos Pérez", 8.5, 9.0)
estudiante1.mostrar_informacion()
