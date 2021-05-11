#declaro la funcion de calculadora
def calculadoraRectangulo(ancho:float,largo:float):
    perimetro = (2 * ancho) +(2 * largo)
    area = ancho * largo
    return "El cuadrado tiene un perimetro de: " +str(perimetro) + " y un area de: "+str(area) #el mensaje retorna cuadrdo porque asi lo estipula el reto.

#capturo por consola los valores del rectangulo y asu vez se fuerzan para que sean de tipo float
#ancho = float(input("Digite el valor del ancho del rectangulo "))
#largo = float(input("Digite el valor del largo del rectangulo "))

mostrar=calculadoraRectangulo(3,2.5)

print(mostrar)