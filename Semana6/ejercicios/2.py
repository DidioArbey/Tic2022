class Triangulo:
    def __init__(self,lado1,lado2,lado3) -> None:
        self.__lado1=lado1
        self.__lado2=lado2
        self.__lado3=lado3
    def lado_mayor(self):
        lista=[self.__lado1,self.__lado2,self.__lado3]
        mayor=max(lista)
        return f"El lado mayor es: {mayor}"
        pass
    def get_tipo(self):
        if self.__lado1 == self.__lado2 == self.__lado3:
            return "equilatero"
        elif self.__lado1 != self.__lado2 != self.__lado3:
            return "escaleno"
        else:
            return "isoceles"

triangulo = Triangulo(3,4,5)
print(triangulo.get_tipo(),triangulo.lado_mayor())

triangulo = Triangulo(3,3,5)
print(triangulo.get_tipo(),triangulo.lado_mayor())

triangulo = Triangulo(5,5,5)
print(triangulo.get_tipo(),triangulo.lado_mayor())