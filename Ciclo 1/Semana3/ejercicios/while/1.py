#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

def alumnos():
    i=1
    mayor7 = menor7 = 0
    while i <= 10:
        nota=float(input(f"Digite la nota del {i} alumno: "))
        if nota >= 7:
            mayor7 += 1
        else:
            menor7 += 1
        i += 1
    print(f"Los alumnos con notas mayor igual a 7 son : {mayor7}")
    print(f"Los alumnos con notas menores a 7 son : {menor7}")

alumnos()


