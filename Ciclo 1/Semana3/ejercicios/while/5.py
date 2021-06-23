#Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
def multiplos():
    i=1
    x = list(range(501))
    while i <= 500:
        #print(f"8 x {i} = {x[i]*8}")
        print(x[i]*8)
        i+=1
multiplos()