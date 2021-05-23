""" En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar
un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
informar el importe que gasta la empresa en sueldos al personal.
 algoritmo
 numeroTrabajdadores
 sueldo= 100 ... 500
 ingresar sueldos trabajador
 sumar sueldos
 si sueldo  entre 100 y 300
    contador1

 si sueldo > 300
    contador2"""
print("Binevenidos a mi empresa")
numeroTrabajadores=int(input("Digite la cantidad de trabajadores que hay en la empresa: "))
def empresa(numeroTrabajadores):
    i=1
    sueldoMenor=sueldoMayor=sueldos=0
    while i <= numeroTrabajadores:
        sueldoTrabajador=int(input(f"digite el sueldo del {i} trabajador: "))
        sueldos += sueldoTrabajador
        if sueldoTrabajador >100 and sueldoTrabajador <=300:
            sueldoMenor+= 1
        else:# sueldoTrabajador >300 and sueldoTrabajador<=500:
            sueldoMayor += 1
        i+=1
    print(f"Los empleados que ganan entre $100 y 300 son: {sueldoMenor}")
    print(f"Los empleados que ganan mas de $300 son: {sueldoMayor}")
    print(f"La empresa gasta un total de: {sueldos} en los empleados")

empresa(numeroTrabajadores)



