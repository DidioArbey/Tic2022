"""A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la
cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las
horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa
ingresadas por el usuario."""

def salarioTrabajador():
    horaTrabajada=float(input("Digite las horas trabajadas: "))
    valorHora=int(input("Digite el valor de la hora: "))
    if horaTrabajada > 40:
        extra= horaTrabajada-40
        saldo=40*valorHora
        sextra= (valorHora*0.5)+valorHora
        saldoextra=extra*sextra
        Pagar=saldo+saldoextra
        print(f"El salario del trabajador sera de: ${Pagar}")
    else:
        saldo=horaTrabajada*valorHora
        print(f"El salario del trabajador sera de: ${saldo}")
print(salarioTrabajador())
