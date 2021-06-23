nombres=[]
edades=[]

for x in range(2):
    nom=input("Ingresar el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("ingrese la edad de dica persona: "))
    edades.append(ed)

print("Nombres de las personas mayores de edad: ")

for x in range(2):
    if edades[x]>=18:
        print(nombres[x])

