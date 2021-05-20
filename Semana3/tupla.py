
def ejercicio():
    respuesta=input("Desea ingresar numeros: ")
    listaNumeros=[]
    while(respuesta != "No"):
        ingresarN=int(input("Ingresar un numero: "))
        listaNumeros.append(ingresarN)
        respuesta=input("Desea ingresar numeros: ")
    tupla=tuple(listaNumeros)
    promedio=sum(tupla)/len(tupla)
    print(promedio)

ejercicio()


