#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
def alturasPersonas():
    i=1
    n=int(input("Digite la cantidad de alturas que desea ingresar: "))
    alturas=[]
    while i <= n:
        altura=float(input(f"ingrese la altura de la {i} persona en metros: "))
        alturas.append(altura)
        i += 1
    alturasNuevas=set(alturas)
    promedio=sum(alturasNuevas)/len(alturasNuevas)
    print(f"El promedio de las alturas en el conjunto es de : {promedio}")
#alturasPersonas()

def ejempl2():
    i=1
    alturas=set()
    promedios=0
    while i >= 1:
        altura=float(input(f"ingrese la altura de la {i} persona en metros: "))
        alturas.add(altura)
        promedios= sum(alturas)/len(alturas)
        print(f"La altura promedio de los {i} es de : {promedios} m \nSi desea finalizar digite una altura de 500")
        i += 1
ejempl2()


