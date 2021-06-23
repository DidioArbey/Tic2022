#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
def digitoMayor():
    numero=int(input("Digite un numero de tres digitos "))
    validar=len(str(numero))
    if validar == 3:
        n1=(int(str(numero)[0]))
        n2=(int(str(numero)[1]))
        n3=(int(str(numero)[2]))
        if n1> n2 and n1>n3:
            print("el primer digito es el mayor")
        elif n2 > n1 and n2 > n3:
            print("el segundo digito es el mayor")
        elif n3>n1 and n3>n2:
            print("El tercer digito es el mayor")
        elif n1==n2 and n2==n3:
            print("Los tres digitos son iguales =(")
    else:
        print("El numero digitado no tiene tres digitos")

print(digitoMayor())