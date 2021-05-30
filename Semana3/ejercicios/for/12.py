""" Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles
(dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo. """
def triangulos(num):
    ladoA=[]
    ladoB=[]
    ladoC=[]
    equilatero=isosceles=escaleno=0
    for i in range(num):
        ladoa=int(input(f"Ingrese el lado a del {i+1} tiangulo: "))
        ladoA.append(ladoa)
        ladob=int(input(f"Ingrese el lado b del {i+1} tiangulo: "))
        ladoB.append(ladob)
        ladoc=int(input(f"Ingrese el lado c del {i+1} tiangulo: "))
        ladoC.append(ladoc)
        if ladoA[i] == ladoB[i] == ladoC[i]:
            equilatero += 1
            print("Es un trieangulo equilátero")
        elif ladoA[i]==ladoB[i] or ladoA[i]==ladoC[i] or ladoC[i]==ladoB[i]:
            isosceles+=1
            print("Es un trieangulo isósceles")
        elif (ladoA[i] != ladoB[i] != ladoC[i]):
            escaleno +=1
            print("Es un trieangulo escaleno")
    print()
    print(f"la cantidad de triangulos equiláteros son: {equilatero}")
    print(f"la cantidad de triangulos isósceles son: {isosceles}")
    print(f"la cantidad de triangulos escaleno son: {escaleno}")




triangulos(3)