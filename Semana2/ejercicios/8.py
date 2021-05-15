#Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
def sumaNumeros():
    numero1=int(input("Digite el primer numero "))
    validar1=len(str(numero1))
    numero2=int(input("Digite el segundo numero "))
    validar2=len(str(numero2))
    if (validar1 == 2) and (validar2 == 2):
        numero1=(int(str(numero1)[0])+int(str(numero1)[1]))
        numero2=(int(str(numero2)[0])+int(str(numero2)[1]))
        resultado=numero1+numero2
        print(f"la suma de todos los digitos es de {resultado}")
    else:
        print("uno o dos de los numeros que digito no tienen dos digitos")

print(sumaNumeros())