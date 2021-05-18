# Leer un número entero menor que 50 y positivo y determinar si es un número primo.
def primo(numero,n=2):
    if numero >=0:
        if numero < 50:
            if n >=numero:
                print("Es primo")
            elif numero % n !=0:
                return primo(numero,n+1)
            else:
                print("No es primo")
        else:
            print("el numero digitado no es menor que 50 ")
    else:
        print("el numero digitado no es positivo ")

numero=int(input("Digite un numero de dos digitos menor que 50: "))
print(primo(numero))