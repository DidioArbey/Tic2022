#Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.

def iguales():
    numero=int(input("Digite un numero de dos digitos "))
    validar=len(str(numero))
    if validar==2:
        num1=int(str(numero)[0])
        num2=int(str(numero)[1])
        if num1 == num2:
            print("Los dos digitos son iguales")
        else:
            print("los dos digitos no son iguales")
    else:
        print("el numero digitado no tiene dos digitos intente de nuevoo \n")


print(iguales())