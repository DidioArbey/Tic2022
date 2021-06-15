#declaro la funcion de calculadora
def calculadoraRectangulo(ancho:float,largo:float)->str:
    perimetro = (2 * ancho) +(2 * largo)
    area = ancho * largo
    mostrar = "El cuadrado tiene un perimetro de: {0:.1f}".format(perimetro) + " y un área de: {0:.1f}".format(area)
    print(mostrar)
    #mensaje2 = f"El cuadarado tiene un perimetro de: {perimetro} y un area de: {area}"
    #print(mensaje2)
    #return mensaje #el mensaje retorna cuadrdo porque asi lo estipula el reto.

#capturo por consola los valores del rectangulo y asu vez se fuerzan para que sean de tipo float
#ancho = float(input("Digite el valor del ancho del rectangulo "))
#largo = float(input("Digite el valor del largo del rectangulo "))

mostrar=calculadoraRectangulo(3,2.5)

#print(mostrar)