"""
Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la
tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36."""
def tablasMultiplicar():
    numero=int(input("Ingrese un numero del 1 al 10: "))

    if numero >= 1 and numero <=10:
        for x in range(1,13):
            resultado=numero*x
            print(resultado ,end=' ')
    else:
        print("El numero digitado no esta en el rango de 1 a 10")
tablasMultiplicar()