def simulador_prestamo_yo_le_presto(datos_prestamo: dict) -> dict:
    saldoFinanciar = datos_prestamo["valor"] + datos_prestamo["gastos documentacion"]
    numeroCuota = datos_prestamo["cuotas"]
    listas=[]
    for i in range(numeroCuota):
        saldoFinanciar += saldoFinanciar # saldoFinanciar= saldoFinaciar + saldoFinaciar
        listas.append((i+1,saldoFinanciar))
    x=10
    peras={
        "llave1": x,
        "llave2": listas #donde coloco mis listas y tuplas
    }
    return peras


arbol={
    "valor": 2000000.0,
    "gastos documentacion":0.0,
    "cuotas":6,
    "interes anual":28.99
}
print(simulador_prestamo_yo_le_presto(arbol))
