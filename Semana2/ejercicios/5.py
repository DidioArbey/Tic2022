#Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
def primo(numero,n=2):
    validar=len(str(numero))
    if numero >= 0:
        if validar==2:
            if numero >=n:
                print("Es primo")
            elif numero % n !=0:
                return primo(numero,n+1)
            else:
                print("No es primo")
        else:
            print("el numero digitado no es de dos digitos")
    else:
        print("El numero digitado no es primo y es negativo")

numero = int(input("Digite un numero "))
print(primo(numero))
