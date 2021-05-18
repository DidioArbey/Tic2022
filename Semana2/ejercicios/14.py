#Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo
def mayor ():
    numero=int(input("Digite un numero de cuatro digitos "))
    validar=len(str(numero))
    if validar == 4:
        n1=(int(str(numero)[1]))
        n2=(int(str(numero)[2]))
        if n1 == n2:
            print("El segundo digito es igual al penúltimo")
        else:
            print("El sgundo digito no es igual al penúltimo")
    else:
        print("El numero digitado no es de cuatro digitos")

print(mayor())