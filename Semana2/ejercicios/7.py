#Leer dos números enteros y determinar cuál es el mayor.


def mayor():
    numero1=int(input("Digite el primer numero "))
    numero2=int(input("Digite el segundo numero "))
    if numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}")
    elif numero2 > numero1:
        print(f"{numero2} es mayor que {numero1}")
    else:
        print("los dos numeros que digito son iguales")

print(mayor())
