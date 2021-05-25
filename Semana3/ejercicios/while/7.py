"""Desarrollar un programa que permita cargar n números enteros y luego nos informe
cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador
retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
if valor%2==0: """

def pares():
    par=impar=0
    n=int(input("Digite la cantidad de numeros a evaluar: "))
    lista1=[]
    i=j=1
    while i<=n:
        lista=int(input(f"Ingresar el {i} numero dela lista : "))
        lista1.append(lista)
        i+=1
    while j <= n:
        #print(lista1[j-1])
        if lista1[j-1] % 2 == 0:
            par+=1
        else:
            impar+=1
        j+=1
    print(f"\nLa cantidad de numeros pares son: {par}")
    print(f"La cantidad de numeros impares son: {impar}")
pares()

