'''numeros=[4,3,2,6,8,10,25,12,5,3,4,6,8,9]
filtroTupla=tuple(filter(lambda numeroPar: numeroPar%2==0, numeros))
filtroLista=list(filter(lambda numeroPar: numeroPar%2==0, numeros))
print(filtro)
filter en listas y tuplas'''
'''
contador=0
listanueva=[{
    "id":"35165",
    "nombre":"alksjdflkj",
    "tipo":"DVD",
    "genero":"Terror"
},
{
    "id":"15665",
    "nombre":"alksjfsdhgsgfhdflkj",
    "tipo":"DVD",
    "genero":"Terror"
},
{
    "id":"456484",
    "nombre":"hspojfio",
    "tipo":"Cd",
    "genero":"Accion"
}]
dvd=filter(lambda esDVD: esDVD["tipo"] =="DVD" ,listanueva)
for esDVD in dvd:
    contador+=1
print(contador)
filter en un diccionario'''