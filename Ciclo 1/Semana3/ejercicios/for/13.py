""" Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar."""
# def cuadrantes():
#     centro=cua1=cua2=cua3=cua4=0
#     puntos= int(input("Ingrese la cantidad del puntos a evaluar: "))
#     for i in range(puntos):
#         CoorX=int(input(f"Ingrese el valor de X de la coordenada {i+1}: "))
#         CoorY= int(input(f"Ingrese el valor de y de la coordenada {i+1}: "))
#         if (CoorX >= 0 and CoorY >= 0):
#             cua1 += 1
#         elif(CoorX < 0 and CoorY >= 0):
#             cua2 += 1
#         elif(CoorX < 0 and CoorY <0):
#             cua3 += 1
#         elif(CoorX >= 0 and CoorY < 0):
#             cua4 += 1

#     print(f"El primer cuadrante tiene: {cua1} puntos")
#     print(f"El segundo cuadrante tiene: {cua2} puntos")
#     print(f"El tercer cuadrante tiene: {cua3} puntos")
#     print(f"El cuarto cuadrante tiene: {cua4} puntos")
# cuadrantes()
def planoCarte():
    cuadrante1,cuadrante2,cuadrante3,cuadrante4=0,0,0,0
    coordenadaX=[]
    coordenadaY=[]
    puntos=int(input("Digite la cantidad de cordenadas que desea evaluar: "))
    for i in range(puntos):
        coorX=float(input(f"Digite el valor de x en la {i+1} cordenada: "))
        coordenadaX.append(coorX)
        coorY=float(input(f"Digite el valor de y en la {i+1} cordenada: "))
        coordenadaY.append(coorY)
        if (coordenadaX[i] >= 0 and coordenadaY[i] >= 0):
            cuadrante1 += 1
        elif(coordenadaX[i] < 0 and coordenadaY[i] >= 0):
            cuadrante2 += 1
        elif(coordenadaX[i] < 0 and coordenadaY[i] <0):
            cuadrante3 += 1
        elif(coordenadaX[i] >= 0 and coordenadaY[i] < 0):
            cuadrante4 += 1
        i += 1
    print(f"El primer cuadrante tiene: {cuadrante1} puntos")
    print(f"El segundo cuadrante tiene: {cuadrante2} puntos")
    print(f"El tercer cuadrante tiene: {cuadrante3} puntos")
    print(f"El cuarto cuadrante tiene: {cuadrante4} puntos")
planoCarte()