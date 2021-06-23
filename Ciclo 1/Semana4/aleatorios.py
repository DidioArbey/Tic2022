from random import randint, randrange, random, uniform
#genrear numero alearotios
#Randint-> genera un num aleatorio entre un valor de inicio y uno final
for num in range(10):
    print(randint(10,100), end=' ')
print()
# randrange -> genera un numero aleatorio con un inicio y un final como parametro opcional se puede colocar una distancia minima entre numeros
for num in range(10):
    print(randrange(10,20, 2), end=' ')
print()
#Ramdom -> genera numero flotante aleatorio entre 0 y 1 pero  no usa el 1
for num in range(10):
    print(random(), end=' ')
print()
#Uniform ->genera un numero flotante aleatorio entre un valor inicial y un valor final 
for num in range(10):
    print(uniform(10,100), end=' ')