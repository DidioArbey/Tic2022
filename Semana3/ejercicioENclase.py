def calculadoraPromedio():
    conjuntoN = input("Ingresar un conjunto de datos separados por coma: ")
    conjuntoNumeros= conjuntoN.split(',')
    conjuntoTupla= tuple(conjuntoNumeros)
    tamanio=len(conjuntoTupla)
    suma=0
    for i in range(tamanio):
        suma += int(conjuntoTupla[i])
    promedio = suma/tamanio
    print(promedio)

calculadoraPromedio()