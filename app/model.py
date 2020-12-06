from pickleshare import *
from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client.SampleCollections

lista_pokemon = []


def loginPickle(usuario, contrasenia):
    db = PickleShareDB('usuarios')

    if usuario in db:
        if db[usuario].get('contrasenia') == contrasenia:
            return True
    return False

def registroPickle(usuario, contrasenia):

    db = PickleShareDB('usuarios')

    if usuario in db:
        return False

    db[usuario] = {'contrasenia': contrasenia}

    return True

def editarPickle(usuario, contrasenia, actual):
    db = PickleShareDB('usuarios')

    if usuario in db:
        return False

    db[usuario] = {'contrasenia': contrasenia}
    del db[actual]

    return True

def mongoAniadir(name, type, height, weight, img):
    lista_pokemon.clear()
    id = 0.0
    numero = 0
    pokemons = db.samples_pokemon.find()
    nombre = name
    tipo = type
    altura = height
    peso = weight
    imagen = img
    success = True
	

    for pokemon in pokemons:
        if nombre == pokemon['name']:
            success = False
        else:
            id = int(pokemon['id'])
            numero = int(pokemon['num'])
                
    id +=+ 1.0
    numero += 1

    nuevoPKM = { "id": id, "num": numero, "name": nombre, "img": imagen, "type": tipo, "height": altura, "weight": peso }
    db['samples_pokemon'].insert(nuevoPKM)

    for pokemon in pokemons:
        if pokemon['name'] == nombre:
            lista_pokemon.append(pokemon)

    return success

def mongoBuscarTipo(type):
    lista_pokemon.clear()
    tipo = type
    pokemons = db.samples_pokemon.find()
	
    for pokemon in pokemons:
        if tipo in pokemon['type']:
            lista_pokemon.append(pokemon)
    
    return lista_pokemon


def mongoBuscarNumero(num):
    lista_pokemon.clear()
    numero = num
    pokemons = db.samples_pokemon.find()
	
    for pokemon in pokemons:
        if numero == pokemon['num']:
            lista_pokemon.append(pokemon)

    return lista_pokemon


def mongoBuscarNombre(name):
    lista_pokemon.clear()
    nombre = name
    pokemons = db.samples_pokemon.find()
	
    for pokemon in pokemons:
        if nombre in pokemon['name']:
            lista_pokemon.append(pokemon)

    return lista_pokemon


def mongoBorrar(name):
    lista_pokemon.clear()
    pokemons = db.samples_pokemon.find()
    nombre = name
    success = False
        
    for pokemon in pokemons:
        if nombre in pokemon['name']:
            db['samples_pokemon'].delete_one(pokemon)
            success = True
                
    return success

def mongoEditar(nameE, NuevoNombreEditar, TipoEditar, AlturaEditar, PesoEditar, ImagenEditar):
    lista_pokemon.clear()
    pokemons = db.samples_pokemon.find()
    nombre = nameE

    for pokemon in pokemons:
        if nombre in pokemon['name']:
            if not NuevoNombreEditar == '':
                nombre = NuevoNombreEditar
            else:
                nombre = pokemon['name']

            if not TipoEditar == '':
                tipo = TipoEditar
            else:
                tipo = pokemon['type']

            if not AlturaEditar == '':
                altura = AlturaEditar
            else:
                altura = pokemon['height']

            if not PesoEditar == '':
                peso = PesoEditar
            else:
                peso = pokemon['weight']
                        
            if not ImagenEditar == '':
                imagen = ImagenEditar
            else:
                imagen = pokemon['img']

            editarPKM = { "$set": { "id": pokemon['id'], "num": pokemon['num'], "name": nombre, "img": imagen, "type": tipo, "height": altura, "weight": peso } }
            db['samples_pokemon'].update_one(pokemon, editarPKM)

            lista_pokemon.append(editarPKM)

    return lista_pokemon

def getLista():
    return lista_pokemon