def simulador_prestamo_yo_le_presto(datos_prestamo: dict) -> dict:
    saldoFinanciar=datos_prestamo["valor"]+datos_prestamo["gastos documentacion"]
    EA=datos_prestamo["interes anual"]/100
    TMV=((1+EA)**(1/12))-1
    cuotas=datos_prestamo["cuotas"]
    cuota=round((TMV*saldoFinanciar)/(1-(1+TMV)**(-cuotas)),0)

    dicionarioNuevo={
        "saldo financiar" : saldoFinanciar,
        "cuota" : cuota,
        "amortizacion": []
    }

    for iterar in range(cuotas):
        vlrInteres= round(saldoFinanciar*TMV,2)
        capAbonado= round(cuota-vlrInteres,2)
        if iterar == cuotas-1:
            capAbonado=saldoFinanciar
        nuevoSaldo= round(vlrInteres+capAbonado,2)
        saldoFinanciar = round(saldoFinanciar-capAbonado,2)
        dicionarioNuevo["amortizacion"].append((iterar+1,capAbonado,vlrInteres,nuevoSaldo,saldoFinanciar))

    return dicionarioNuevo