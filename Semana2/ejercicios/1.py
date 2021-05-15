# Leer un número entero y determinar si es un número terminado en 4. 
def terminadoCuatro():
    numero = int(input("Digite un numero "))
    ultimoNumero = int(str(numero)[-1]) #str para convertir en una cadena y asi poder evaluar su ultima posicion
    if ultimoNumero == 4:
        print("el numero termina en 4")
    else:
        print("el numero no termina en 4")

mensaje=terminadoCuatro()
print(mensaje)
