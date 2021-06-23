#Escribir una funcion que pregunte al usuario un conjunto de numeros, los almacene eun una lista y los muestre por pantalla ordenados de menor a mayor
def ordenarListaM():
    respuesta=input("Desea ingresar numeros: ")
    listaNumeros=[]
    while(respuesta != "No"):
        ingresarN=int(input("Ingresar un numero: "))
        listaNumeros.append(ingresarN)
        respuesta=input("Desea ingresar numeros: ")
    listaNumeros.sort()
    print(listaNumeros)

ordenarListaM()