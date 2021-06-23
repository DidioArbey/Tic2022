#Programacion orientada a objetos
class Persona:
    def __init__(self,nombre, apellido,edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Didio","Perdomo",25)
print(persona1, type(persona1))


persona2= Persona("Cesar","Diaz",25)
print(persona2, type(persona2))
