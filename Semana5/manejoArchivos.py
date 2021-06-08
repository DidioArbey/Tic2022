#crear un archivo nuevo.
#modo w es para escribir
def crearArchivoEjemplo(nombreArchivo="prueba1.txt"):
    archivo = open(nombreArchivo, "w")

    archivo.write("Hola Mundo")
    archivo.write("\n")
    archivo.write("Este es mi primer archivo\n")
    archivo.write("ultima linea\n")
    archivo.write(str(5+1))
#crearArchivoEjemplo()

#modo r es leer
#lectura con modo r
def leerArchivo(nombreArchivo="prueba1.txt"):
    archivo = open(nombreArchivo, "r")

    for linea in archivo:
        #print(linea)
        print(linea.strip("\n"))#strip es para quitar espacios o modificar un caracter
    archivo.close()
    print("archivo leido!")
#leerArchivo()

#modo a para agregar

def crearArchivoEjemplo2(mensaje="Hola mundo", nombrearchivo="prueba1.txt"):
    archivo = open(nombrearchivo, "a")
    print(mensaje, file=archivo)
    archivo.close()
crearArchivoEjemplo2(f"Nueva linea de texto {10**3}")


#lectura con whit

