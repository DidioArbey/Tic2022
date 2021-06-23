# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)
def serie():
    i=1
    x = list(range(100))
    while i <= 25:
        print(f"iteracion {i} es: {x[i]*11}")
        i+=1
serie()