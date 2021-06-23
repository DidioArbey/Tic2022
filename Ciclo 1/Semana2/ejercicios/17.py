#Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.
def parImpar():
    numero=int(input("Digite un numero entero de 4 digitos: "))
    validar=len(str(numero))
    numeroPar=0
    numeroImpar=0
    if validar==4:
        n1=(int(str(numero)[0]))
        n2=(int(str(numero)[1]))
        n3=(int(str(numero)[2]))
        n4=(int(str(numero)[3]))
        if n1 % 2==0:
            numeroPar=numeroPar+1
        else:
            numeroImpar=numeroImpar+1
        if n2 % 2==0:
            numeroPar=numeroPar+1
        else:
            numeroImpar=numeroImpar+1
        if n3 % 2==0:
            numeroPar=numeroPar+1
        else:
            numeroImpar=numeroImpar+1
        if n4 % 2==0:
            numeroPar=numeroPar+1
        else:
            numeroImpar=numeroImpar+1
        if numeroPar > numeroImpar:
            print("El numero digitado tiene mas digitos pares")
        elif numeroPar < numeroImpar:
            print("El numero digitado tiene mas digitos impares")
        else:
            print("Los numero digitado tiene la misma cantidad de impares que de pares")
    else:
        print("El numero digitado no tiene 4 digitos")

print(parImpar())



