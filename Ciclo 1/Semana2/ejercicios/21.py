""" Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
del rango permitido."""
def promedioEstudiante():
    print("las notas a digitar deben estar entre 0 a 5")
    nota1=float(input("Digite la primera nota: "))
    nota2=float(input("Digite la primera nota: "))
    nota3=float(input("Digite la primera nota: "))
    if (nota1 >=0 and nota1<=5) and (nota2 >=0 and nota2<=5) and ((nota3 >=0 and nota3<=5)):
        promedio=(nota1+nota2+nota3)/3
        if promedio > 3:
            print(f"El estudiante aprobo con una nota de {promedio}")
        else:
            print("El estudiante No aprobo la materia debe de tener una nota mayor q 3")
    else:
        print("una de las notas ingresadas no esta en el rango para ser evaludado")

print(promedioEstudiante())