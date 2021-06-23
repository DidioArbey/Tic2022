#16. Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
#Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""

def cargarOracion():
    oracion = input("Escribir una oración: ")
    cantidadEspacio = 0
    for x in range(len(oracion)):
        if oracion[x]==" ":
            cantidadEspacio += 1
        else:
            cantidadEspacio += 0
    print("Cantidad de espacios en blanco: ", cantidadEspacio)

#cargarOracion()

#17. Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
#Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas
#para que sea más fácil disponer la condición que verifica que es una vocal.
def contarVocales():
    oracion = input("Escribir una oración: ")
    oracionMinuscula = oracion.lower()
    cantidadVocales = 0
    for x in range(len(oracionMinuscula)):
        if oracionMinuscula[x]=="a" or oracionMinuscula[x]=="e" or oracionMinuscula[x]=="i" or oracionMinuscula[x]=="o" or oracionMinuscula[x]=="u":
            cantidadVocales += 1
        else:
            cantidadVocales += 0
    print("Cantidad de vocales en la oración son: ", cantidadVocales)

contarVocales()