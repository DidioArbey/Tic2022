def  calculadoraRectangulo(ancho: float, largo:float)->str:
    perimetro = (ancho*2) + (largo*2)
    area= (largo*ancho)
    mostrar=("El cuadrado tiene un perimetro de:{0:.1f}".format(perimetro) + " y un área de:{0:.1f}".format(area))
    print(mostrar)
mostrar=calculadoraRectangulo(3,2.5)

