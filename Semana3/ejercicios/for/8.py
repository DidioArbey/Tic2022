"""Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la
medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12. a->(b*h)/2"""
def superficieTriangulo():
    n=int(input("Digite la cantidad de triangulos a evaluar: "))
    base=[]
    altura=[]
    area=[]
    mayor=0
    for x in range(n):
        b=float(input("Digite la base del triangulo: "))
        base.append(b)
        h=float(input("Digite la altura del triangulo: "))
        altura.append(h)
        a=(b*h)/2
        area.append(a)
    for contador in range(n):
        print(f"Para el {contador+1} triangulo su base es de: {base[contador]} su altura es de: {altura[contador]} y su superficie es de: {area[contador]}")
        if area[contador] > 12:
            mayor+=1
    print(f"El numero de triangulos con una superficie mayor de 12 es: {mayor}")

superficieTriangulo()