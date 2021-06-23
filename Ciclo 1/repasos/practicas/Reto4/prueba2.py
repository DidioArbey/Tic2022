
from datetime import date

# def esDVD(pelicula):
#     return pelicula["tipo"] == "DVD"
xDVD=(lambda pelicula:pelicula["tipo"]=="DVD")

def eliminarPelicula(pelicula):
    genero = pelicula["genero"]
    if xDVD and (genero == 'Acción' or genero == 'Comedia' or genero == 'Drama'):
        return False
    elif xDVD and genero == 'Terror':
        if date.today().year - pelicula["año"] > 20: # tiene más de 20 años
            return True
    elif not xDVD:
        if genero == 'Terror' and (date.today().year - pelicula["año"] > 10): # tiene más de 20 años
            return True
        elif date.today().year - pelicula["año"] > 15:
            return True
    return False

def invertirNombreApellido(actor: str):
    nombres = actor.lstrip().rstrip().split(" ")
    return nombres[1] + ',' + nombres[0]

def catalogacion_peliculas(inventario: list):
    newlist = list()
    DVDsEliminados = list()
    CDsEliminados = list()
    for item in inventario:
        if eliminarPelicula(item):
            if xDVD(item):
                DVDsEliminados.append(item["id"])
            else:
                CDsEliminados.append(item["id"])
        else:
            actores = str(item["actor"]).split(",")
            actores = map(invertirNombreApellido, actores)
            item["actor"] = ";".join(actores)
            newlist.append(item)
    tuplaSalida= tuple((newlist, DVDsEliminados, CDsEliminados))
    return tuplaSalida


inventario = [
    {'id': '45125',
    'titulo': 'The Shawshank Redemption',
    'tipo': 'DVD',
    'genero': 'Drama',
    'actor': 'Tim Robbins,Morgan Freeman,Bob Gunton',
    'año':1994,
    'duración': '2h22min'},

    {'id': '54217',
    'titulo': 'The Dark Knight',
    'tipo': 'DVD',
    'genero': 'Acción',
    'actor': 'Christian Bale,Heath Ledger,Aaron Eckhart',
    'año': 2008,
    'duración': '2h32min'},

    {'id': '63587',
    'titulo': 'El bueno,El malo y El feo',
    'tipo': 'DVD',
    'genero': 'Acción',
    'actor': 'Clint Eastwood,Eli Wallach,Lee VanCleef',
    'año': 1996,
    'duración': '2h41min'},

    {'id':'75698',
    'titulo': 'Forrest Gump',
    'tipo':'DVD',
    'genero': 'Comedia',
    'actor': 'Tom Hanks',
    'año': 1994,
    'duración': '2h22min'},

    {'id': '87556',
    'titulo': 'Alien - El octavo pasajero',
    'tipo': 'DVD',
    'genero': 'Terror',
    'actor': 'Sigourney Weaver,Tom Skerritt',
    'año': 1994,
    'duración': '1h57min'},

    {'id': '96587','titulo': 'El gran dictador',
    'tipo': 'CD',
    'genero': 'Comedia',
    'actor':'Charles Chaplin',
    'año': 1940,
    'duración':'2h5min'}
    ]

print(catalogacion_peliculas(inventario))