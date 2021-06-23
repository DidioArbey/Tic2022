# Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
def mayorDigito():
    numero1=int(input("Digite el primer numero de dos digitos "))
    numero2=int(input("Digite el segundo numero de dos digitos "))
    numero3=int(input("Digite el tercer numero de dos digitos "))
    validar1=len(str(numero1))
    validar2=len(str(numero2))
    validar3=len(str(numero3))
    if (validar1==2)and(validar2==2)and(validar3==2):
        #n1=(int(str(numero)[0]))
        n1=(int(str(numero1)[0]))
        n2=(int(str(numero1)[1]))
        n3=(int(str(numero2)[0]))
        n4=(int(str(numero2)[1]))
        n5=(int(str(numero3)[0]))
        n6=(int(str(numero3)[1]))
        if (n1 > n2) and (n1 > n3) and (n1 > n4) and (n1 > n5) and (n1 > n6):
            print(f" {n1} es el digito mayor")
        elif (n2 > n1) and (n2 > n3) and (n2 > n4) and (n2 > n5) and (n2 > n6):
            print(f" {n2} es el digito mayor")
        elif (n3 > n1) and (n3 > n2) and (n3 > n4) and (n3 > n5) and (n3 > n6):
            print(f" {n3} es el digito mayor")
        elif (n4 > n1) and (n4 > n2) and (n4 > n3) and (n4 > n5) and (n4 > n6):
            print(f" {n4} es el digito mayor")
        elif (n5 > n1) and (n5 > n3) and (n5 > n4) and (n5 > n2) and (n5 > n6):
            print(f" {n5} es el digito mayor")
        elif (n6 > n1) and (n6 > n3) and (n6 > n4) and (n6 > n5) and (n6 > n2):
            print(f" {n6} el sexto digito es el digito mayor")
        else:
            print("Todos los digitos son iguales")
    else:
        print("Uno o todos los numeros digitados no tienen de ha dos digitos cada uno")

print(mayorDigito())