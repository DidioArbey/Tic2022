#Leer tres números enteros y determinar si el último dígito de los tres números es igual.
def finalIgual():
    numero1=int(input("Digite el primer numero entero: "))
    numero2=int(input("Digite el segundo numero entero: "))
    numero3=int(input("Digite el tercer numero entero: "))
    ultimoNumero1 = int(str(numero1)[-1])
    ultimoNumero2 = int(str(numero2)[-1])
    ultimoNumero3 = int(str(numero3)[-1])
    if (ultimoNumero1 == ultimoNumero2) and(ultimoNumero1==ultimoNumero3):
        print("el ultimo digito de los tres numeros es igual")
    else:
        print("los ultimos digitos no son iguales para los 3 numeros")

print(finalIgual())
