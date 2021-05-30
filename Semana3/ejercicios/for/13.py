""" Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar."""
def cuadrantes():
    centro=cua1=cua2=cua3=cua4=0
    puntos= int(input("Ingrese la cantidad del puntos a evaluar: "))
    for i in range(puntos):
        CoorX=int(input(f"Ingrese el valor de X de la coordenada {i+1}: "))
        CoorY= int(input(f"Ingrese el valor de y de la coordenada {i+1}: "))
        if (CoorX >= 0 and CoorY >= 0):
            cua1 += 1
        elif(CoorX < 0 and CoorY >= 0):
            cua2 += 1
        elif(CoorX < 0 and CoorY <0):
            cua3 += 1
        elif(CoorX >= 0 and CoorY < 0):
            cua4 += 1

    print(f"El primer cuadrante tiene: {cua1} puntos")
    print(f"El segundo cuadrante tiene: {cua2} puntos")
    print(f"El tercer cuadrante tiene: {cua3} puntos")
    print(f"El cuarto cuadrante tiene: {cua4} puntos")
cuadrantes()