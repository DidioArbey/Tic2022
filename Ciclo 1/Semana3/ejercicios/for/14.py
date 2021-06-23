"""Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares."""
def numeros():
    contNeg, contPos, contMult, par = 0,0,0,0
    for i in range(10):
        num=int(input(f"Ingrese el valor entero {i+1}: "))
        if (num >= 0):
            contPos +=1
        else:
            contNeg += 1
        if(num % 15 == 0):
            contMult += 1
        if(num % 2==0):
            par= par + num
    print(f"Cantidad de valores negativos: {contNeg} ")
    print(f"Cantidad de valores posotivos: {contPos} ")
    print(f"Cantidad de múltiplos de 15: {contMult} ")
    print(f"Suma de numeros pares: {par}")
numeros()