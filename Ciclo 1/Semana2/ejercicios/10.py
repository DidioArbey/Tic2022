#Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros
def multiplo():
    numero=int(input("Digite un numero de tres digitos "))
    validar=len(str(numero))
    if validar == 3:
        n1=(int(str(numero)[0]))
        n2=(int(str(numero)[1]))
        n3=(int(str(numero)[2]))
        if (n1 % n2 == 0) and (n1 % n3 == 0):
            print (f"{n1} es multiplo de los otros dos digitos")
        elif(n2 % n1 == 0) and (n2 % n3 == 0):
            print (f"{n2} es multiplo de los otros dos digitos")
        elif(n3 % n1 == 0) and (n3 % n2 == 0):
            print (f"{n3} es multiplo de los otros dos digitos")
    else:
        print("No es un numero de tres digitos")

print(multiplo())