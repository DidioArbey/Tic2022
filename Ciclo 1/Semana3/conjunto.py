#es parecido al diccionario pero sin {}  los conjunto son imutables igual que las tuplas
#Para un conjunto no se puede ingresar por un indice y toca hacerlo por un cilo
#los conjuntos eliminan los datos iguales
s = set() #Conjunto inmutable

s1= set([1,2,3,4])
s2= set(range(10))
#print(s1[0])
#rint (s1)
#print (s2)
miConjunto={1,3,2,9,3,1}#elimina los iguales 1,3
print(miConjunto)
for numero in miConjunto:
    print(numero)