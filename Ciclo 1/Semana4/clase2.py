from pprint import pprint as pp
from random import randint, randrange, random, uniform
"""def distanciaCiudad():
    listaCiudad=['a','b','c','d','e']
    arcos1={}
    for i in listaCiudad:
        auxCiudades=[]
        for j in listaCiudad:
            if i != j:
                auxCiudades.append((i,j))
        arcos[i]=auxCiudades
    print(arcos1)"""

listaCiudad=['a','b','c','d','e']#(a,b) (a,c) (a,d) (a,e) (b,a) (b,c) (b,d)...(e,d)
arcos={i:[(i,j) for j in listaCiudad]for i in listaCiudad }
pp(arcos) #PP: Prettyprinter, Dar formato a ala salida

def auxArcos():
    auxArcos=[]
    i= 0
    for fila in arcos:
        aux= fila[i:len(fila)]#revanada de una matriz
        if aux != []: #validar si esta vacia no agregar
            auxArcos.append(aux)
        i += 1
    return auxArcos

