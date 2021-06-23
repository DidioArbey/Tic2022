"""Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio
de edades mayor. """
def edades():
    proMañ, proTar, proNoc= 0,0,0
    print("TURNO MAÑANA")
    for i in range(5):
        edad=int(input(f"Ingrese la edad del estudiante {i+1}: "))
        proMañ = (proMañ + edad)
    proMañ= proMañ/5
    print(f"El promedio del turno de la mañana es: {proMañ}")

    print("TURNO TARDE")
    for i in range(6):
        edad=int(input(f"Ingrese la edad del estudiante {i+1}: "))
        proTar = (proTar + edad)
    proTar= proTar/6
    print(f"El promedio del turno de la tarde es: {proTar}")

    print("TURNO NOCHE")
    for i in range(11):
        edad=int(input(f"Ingrese la edad del estudiante {i+1}: "))
        proNoc = (proNoc + edad)
    proNoc= proNoc/11
    print(f"El promedio del turno de la tarde es: {proNoc}")

    if (proMañ > proTar) and (proMañ > proTar):
        print("El turno de la mañana tiene el promedio de edades mayor")
    elif(proTar > proMañ) and (proTar > proNoc):
        print("El turno de la tarde tiene el promedio de edad mayor")
    elif(proNoc > proMañ) and (proNoc > proTar):
        print("El turno de la noche tiene el promedio de edad mayor")
    elif(proMañ==proTar==proNoc):
        print("Los tres turnos tiene el mismo promedio")
edades()