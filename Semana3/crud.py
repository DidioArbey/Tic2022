# Inicializacion de tarea
tareas={
    '01':{
        'descripcion': 'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },
    '02':{
        'descripcion': 'Estudiar',
        'estado': 'pendiente',
        'tiempo': 180
    },
    '03':{
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50
    }
}
#Create
if opcion == 1:
    print()
    print("-> Adicionando Tarea")

    identificador = str(input("Ingrese identificador de la tarea: "))
    descripcion = str(input("Ingrese descripcion de la tarea: "))
    estado = str(input("Ingrese estado inicial de la tarea: "))
    tiempo = int(input("Ingrese tiempo de realizacion: "))

    tareaNueva={
        'descripcion': descripcion,
        'estado': estado,
        'tiempo': tiempo
    }
#Adicionar la tarea
    tareas=create(tareas,identificador,tareaNueva)
#Read
elif opcion==2:
    print()
    print("->Listado de tareas")
    print()
    #Lectura de tareas
    read(tareas)
#Update
elif opcion==3:
    print()
    print("->Actualizar Tarea")
    #solicitar al usuario el identificador
    identificador=str(input("ingrese identificador de la trea para modificar: "))
    #revisar si se encuentra el elemento solicitado
    if


#funcion de crear
def create(tareas,identificador,tareaNueva):
    tareas[identificador]=tareaNueva
    return tareas

def read(tareas):
    for indentificador, tarea in tareas.items():
        print(identificador,'-',end='')
        for nombreAtributo,atributo in tarea.items():
            print(atributo, '-', end='')
        print()

