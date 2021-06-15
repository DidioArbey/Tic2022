from pprint import pprint as pp
def simulador_prestamo_yo_le_fio(datos_prestamo: dict) -> dict:
    #diccionario entrante
    saldoFinanciar=datos_prestamo["valor"]+datos_prestamo["gastos documentacion"]
    EA=datos_prestamo["interes anual"]/100
    #variables
    TMV=((1+EA)**(1/12))-1
    cuotas=datos_prestamo["cuotas"]
    cuota=(TMV*saldoFinanciar)/(1-(1+TMV)**(-cuotas))

    #vlrInteres= saldoFinanciar*TMV
    #capAbonado= cuota-vlrInteres
    #nuevoSaldo= saldoFinanciar-capAbonado
    amortizacion=[]

    #ciclos
    for iterar in range(cuotas):
        #cuota
        amortizacion.append(iterar+1)
        #valor interes
        vlrInteres= saldoFinanciar*TMV
        amortizacion.append(vlrInteres)
        #capital abonado
        capAbonado= cuota-vlrInteres
        amortizacion.append(capAbonado)
        #nuevo saldo
        nuevoSaldo= saldoFinanciar-capAbonado
        amortizacion.append(nuevoSaldo)
    amortizacion2=tuple(amortizacion)

    #Diccionario
    dicionarioNuevo={
        "saldo financiar" : saldoFinanciar,
        "cuota" : cuota,
        "amortizacion": [amortizacion2]
    }
    return dicionarioNuevo

diccioonario={
    "valor": 2000000.0,
    "gastos documentacion":0.0,
    "cuotas":6,
    "interes anual":28.99
}
print(simulador_prestamo_yo_le_fio(diccioonario))