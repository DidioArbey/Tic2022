class Alumno:
    def __init__(self,nombre="",nota=0.0) -> None:
        self.__nombre=nombre
        self.__nota=nota
    
    def resultado(self):
        if self.__nota >= 3.0:
            return "Aprobado"
        return "Reprobado"

alumno=Alumno("Arbey perdomo", 5.0)
print(alumno.resultado())