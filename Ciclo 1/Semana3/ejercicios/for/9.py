"""Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados."""
def yiyo():
    lista=[]
    for x in range(10):
        valores=int(input(f"Ingrese el {x+1} numero: "))
        lista.append(valores)
    i=sum(lista[4:10])
    print(i)
yiyo()