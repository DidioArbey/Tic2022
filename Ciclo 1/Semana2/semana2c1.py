def saludo(nombre):
    return "Hola {}! como estas ".format(nombre)


nombre = input("Ingrese su nombre ")

texto_saludo = saludo(nombre)

print(texto_saludo)