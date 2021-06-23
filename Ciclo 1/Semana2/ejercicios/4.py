#Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
def primo(numero,n=2):
    validar=len(str(numero))
    if validar==2:
        if numero < 20:
            if n >=numero:
                print("Es primo")
            elif numero % n !=0:
                return primo(numero,n+1)
            else:
                print("No es primo")
        else:
            print("el numero digitado no es menor que 20 ")
    else:
        print("el numero digitado no tiene dos digitos ")

numero=int(input("Digite un numero de dos digitos menor que 20: "))
print(primo(numero))
