#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

def pedirNumero():
    numero=int(input("Digite un numero de dos digitos "))
    validar=len(str(numero))
    if validar==2:
        num1=int(str(numero)[0])#2
        num2=int(str(numero)[1])#5
        if (num1 % 2 == 0) and (num2 % 2 == 0):
            print("los dos digitos del numero son pares")
        else:
            print("uno o dos de los digitos son impares")
    else:
        print("el numero digitado no tiene dos digitos ")

mensaje=pedirNumero()
print(mensaje)

