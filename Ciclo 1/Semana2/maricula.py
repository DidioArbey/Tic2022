def pagoMatricula(tipoEstudiante):
    smv =908526
    if tipoEstudiante ==1:
        valorPagar = (2*smv)*0.1
        matricula = valorPagar+(2*smv)
        print(f"usted debe de pagar: {matricula}")
    elif tipoEstudiante==2:
        valorPagar = (3*smv)*.2
        matricula = valorPagar +(3*smv)+120000
        print(f"usted debe de pagar: {matricula}")
    elif tipoEstudiante ==3:
        voto=int(input("Digite \n1 si usted voto o \n2 si usted no voto\n"))
        if voto ==1:
            valorPagar=(5*smv)*0.1
            matricula=(5*smv)-valorPagar
            print(f"usted debe de pagar: {matricula}")
        else:
            matricula= 5*smv
            print(f"usted debe de pagar: {matricula}")
    else:
        print("Dato incorrecto")

tipoEstudiante=int(input("Bienvenido Digite \n1 si es estudiante de pregrado\n2 si es estudiante de especializacion y\n3 si es estudiante de posgrado\n"))

print(pagoMatricula(tipoEstudiante))
