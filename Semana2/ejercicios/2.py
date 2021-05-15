#Leer un número entero y determinar si tiene 3 dígitos.
def tresDigitos():
    numero=int(input("Digite un numero"))
    digitos=len(str(numero)) #len para que me devuelva la longitud de la cadena y asi poder evaluar
    if digitos == 3:
        print("El numero digitado tiene 3 digitos")
    else:
        print("El numero digitado no tiene tres digitos")

mensaje=tresDigitos()
print(mensaje)