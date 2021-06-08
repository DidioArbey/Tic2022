#JSON Javascript Object Notation
import json #biblioteca para trabajar archivos JSON
def crearArchivos(nombreArchivo="usuarios.json"):
    datos=[{
        "nombre": "Arbey Perdomo",
        "email" : "arbey.perdomo99@live.com",
        "edad": 25,
        "profesor" : False
    },
    {
        "nombre": "Cesar Diaz",
        "email" : "cesar.a.diaz@gmail.com",
        "edad": 41,
        "profesor" : True
    }]
    with open(nombreArchivo, "w") as archivo:
        json.dump(datos,archivo, indent=2)#,indent=2 es para identar el json
crearArchivos()

#leer json

def leerArchivo():
    with open ("usuarios.json") as archivo:
        datos= json.load(archivo)
        for dato in datos:
            print(dato, type(dato))
leerArchivo()

