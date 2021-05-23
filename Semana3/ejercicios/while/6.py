"""Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con
un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1
mayor", "Lista 2 mayor", "Listas iguales") Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo. """
def comparacion():
    """
    lista1=[]
    lista2=[]
    i=j=1
    while i<=15:
        lista=int(input(f"Ingresar el {i} numero dela lista 1: "))
        lista1.append(lista)
        i+=1
    print("\n\n")
    while j<=15:
        listas=int(input(f"Ingresar el {j} numero dela lista 2: "))
        lista2.append(listas)
        j+=1
    """
    total1=sum(lista1)
    total2=sum(lista2)
    if total1 > total2:
        print("Lista 1 mayor")
    elif total1 < total2:
        print("Lista 2 mayor")
    else:
        print("Listas iguales")

lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
comparacion(lista1,lista2)
