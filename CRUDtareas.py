tareas = {
    '01': {
        'descripcion': 'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },

    '02': {
        'descripcion': 'Estudiar',
        'estado': 'pendiente',
        'tiempo': 180
    },

    '03': {
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50
    }
}

# Función de crear
def create(tareas, identificador, tareaNueva):
    tareas[identificador] = tareaNueva
    return tareas

# Función leear
def read(tareas):
    for identificador, tarea in tareas.items():
        print(identificador, '-', end='')
        for nombre_atributo, atributo in tarea.items():
            print(atributo, '-', end='')
        print()

# Funciónes Actualizar
def estaElemento(identificador, tareas):
    # Extraer de la base de datos (contenedor) los identificadores
    conjuntoIdentificadores = set(tareas.keys())
    # Revisar si se encuentra el elemento solicitado
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

def update(tareas, identificador):
    pass


mainloop = True
while mainloop:
    print()
    print()
    print('----Aplicación CRUD Tareas Pendientes ----')
    print('------------------------------------------')
    print('-1- Adicionar Tarea')
    print('-2- Consultar Tarea')
    print('-3- Actualizar Tarea')
    print('-4- Eliminar Tarea')
    print('-5- Salir')
    print()

    opcion = int(input('Ingrese una opc: '))

    # -------------> CREATE <-------------------
    if opcion == 1:
        print()
        print("-> Adicionando Tarea")
        identificador = str(input("Ingrese identificador de la tarea: "))
        descripcion = str(input("Ingrese descripcion de la tarea: "))
        estado = str(input("Ingrese estado inicial de la tarea: "))
        tiempo = int(input("Ingrese tiempo de realizacion: "))
        tareaNueva = {
            'descripcion': descripcion,
            'estado': estado,
            'tiempo': tiempo
        }
        # Adicionar la tarea
        tareas = create(tareas, identificador, tareaNueva)
        print("La tarea se creado exitosamente!!")

    # -------------> READ <-------------------
    elif opcion == 2:
        print()
        print("->Listado de tareas")
        print()
        # Lectura de tareas
        read(tareas)

    # ------------> UPDATE <-------------------
    elif opcion == 3:
        print()
        print("->Actualizar tarea")
        print()
        # Solicitar al usuario el identificador
        identificador = str(
            input("Ingrese identificador de la Tarea para modificar: "))
        # Revisar si se encuentra el elemento solicitado
        if estaElemento(identificador, tareas):
            # Actualizar
            # Modificar los campor de interes
            nuevaDescripcion = str(input('Nueva descripcion: '))
            if nuevaDescripcion:
                tareas[identificador]['descripcion'] = nuevaDescripcion
            nuevoEstado = str(input('Nuevo estado:'))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = input('Nuevo tiempo: ')
            if nuevoTiempo:
                nuevoTiempo = int(nuevoTiempo)
                tareas[identificador]['tiempo'] = nuevoTiempo
        else:
            print("No ha sido encontrada la tarea")

    # -----------------> DELETE <-------------------
    elif opcion == 4:
        print()
        print("->Eliminar tarea")
        print()
        # Solicitar al usuario el identificador
        identificador = str(
            input("Ingrese indentificador de la tarea para eliminar: "))
        # Extraer de la base de datos (contenerdor) los identificadores
        conjuntoIdentidificadores = set(tareas.keys())
        # Revisar si se encuenta el elemento solicitado
        if identificador in conjuntoIdentidificadores:
            tareas.pop(identificador)   # proceder a eliminar
            print("Tarea eliminada exitosamente!!")
        else:
            print("No ha sido encontrada la Tarea para eliminar!!")

    elif opcion == 5:
        print("Ha salido exitosamente.")
        break

    else:
        print("Valor Invalido")
