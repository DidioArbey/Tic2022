def mostrarMoneda():
    moneda = {'Euro':'€', 'Dollar':'USD', 'Peso':'$'}
    tipo_moneda = input("Ingrese el tipo de moneda: ")
    if tipo_moneda in moneda:
        print(moneda[tipo_moneda])
    else:
        print("No esta la moneda")

print(mostrarMoneda())


