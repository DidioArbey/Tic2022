def funcion(nombre, peso, altura):
    imc=(peso)/altura**2
    if imc > 50:
        valor=170000
        programa="intermedio"
    elif imc <50:
        valor=120000

    diccionario={
        "nombre":nombre,
        "peso": peso,
        "altura":altura,
        "imc": str(imc),
        "valor":valor
        "programa": programa
    }

    
    return diccionario


print(funcion("diego",65,1.83))