#Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
def primo():
    numero=int(input("Digite un numero de dos digitos menor que 20 "))
    validar=len(str(numero))
    if validar==2:
        if numero < 20:
            pass
        else:
            print("el numero digitado no es menor que 20 intente de nuevo\n")
            print(primo())
    else:
        print("el numero digitado no tiene dos digitos intente de nuevo\n")
        print(primo())

mensaje = primo()
print(mensaje)

#pendiente para evaluar sin usar un cilo for