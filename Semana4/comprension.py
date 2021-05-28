def pares3(limite:int)->list:
    listaPares3=[]
    for num in range(limite+1):
        if num %2==0:
            if num%3==0:
                listaPares3.append(num)
    return listaPares3

#print(pares3(100))

#listaCompresion=[definicionElementoAgregar for variable in otralista]
listaCompresion=[num*3 for num in [1,2,3,4,5,6,7,8,9]]
# listaCompresion=[num*3 for num in [1,2,3,4,5,6,7,8,9]] -> multiplican por 3  los numeros de la lista ya que asi se estipula en la linea
#print(listaCompresion)
#listPares3=[]

diametros=[2,4,6,8,10,12,14,16]
radios=[]
def radiosLista(listaDiametros:list)->list:
    for dia in diametros:
        radio=dia/2
        radios.append(radio)
    return radios
listaPares3=[num for num in range(101) if num %2 == 0 if num%3==0 ]

#print(radiosLista(diametros))

radios=[dia/2 for dia in diametros]
#print(radios)

d1=[2,3,4,5,6,7,8,9]
d2=[3,4,5,6,7,8,9,10]
areas=[d1[i] * d2[i] /2 for i in range(len(d1))]
#print(areas)
