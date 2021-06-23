#Leer un número entero menor que mil y determinar cuántos dígitos tiene.
def menorMil():
    numero=int(input("Digite un numero entero menor de mil: "))
    if numero <= 1000:
        validar=len(str(numero))
        print(f"el numero digitado tiene {validar} digitos")
    else:
        print("El numero digitado no es menor a mil")
print(menorMil())

