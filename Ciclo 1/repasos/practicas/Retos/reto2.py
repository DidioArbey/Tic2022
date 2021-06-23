def calcularSerie(nombre, peso, altura) :
    nombres=nombre.upper()
    imc=peso/(altura**2)
    imc=round(imc,1)
    estructuraGym={
    "nombre":nombres,
    "peso": peso,
    "altura": altura,
    "imc": str(imc),
    }
    if imc < 18.5 or imc >30 :
        estructuraGym['programa']="principiante"
        estructuraGym['valor']=150000
    elif imc >=25 and imc < 29.9:
        estructuraGym['programa']="intermedio"
        estructuraGym['valor']=170000
    elif imc >=18.5 and imc < 24.9:
        estructuraGym['programa']="plus"
        estructuraGym['valor']=200000

    print (estructuraGym)

calcularSerie("didio",74,1.68)