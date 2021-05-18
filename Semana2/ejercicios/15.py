#Leer un número entero y determinar si es múltiplo de 7.
def multiplos():
    numero=(int(input("Digite un numero entero: ")))
    if numero % 7 == 0:
        print("es multiplo de 7")
    else:
        print("no es multiplo de 7")

print(multiplos())