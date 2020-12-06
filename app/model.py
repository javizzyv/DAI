from pickleshare import *
from pymongo import MongoClient
from bson import ObjectId
from flask import jsonify

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
                
    id += 1.0
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


def sigNum():
    pokemons = db.samples_pokemon.find()
    numero = 0

    for pokemon in pokemons:
        numero = int(pokemon['num'])
                
    numero += 1

    return numero

def sigID():
    pokemons = db.samples_pokemon.find()
    id = 0.0

    for pokemon in pokemons:
        id = int(pokemon['id'])
                
    id += 1.0
    
    return id


def buscarListaGet(buscarG):
    lista = []
    buscar = buscarG
    pokemons = db['samples_pokemon'].find(buscar).sort('name')

    for pokemon in pokemons:
            lista.append({
                  'id':    str(pokemon.get('_id')), # pasa a string el ObjectId
                  'nombre': pokemon.get('name'), 
                  'tipo':  pokemon.get('type'),
                  'numero':  pokemon.get('num')
                })
    
    return jsonify(lista)


def buscarIdGet(id):
    try:
        pokemon = db['samples_pokemon'].find_one({'_id':ObjectId(id)})
        return jsonify({
            'id':       id,
            'nombre':   pokemon.get('name'), 
            'tipo':     pokemon.get('type'),
            'numero':   pokemon.get('num')
        })
    except:
        return jsonify({'error':'Not found'}), 404

def aniadirPost(nom, tip, alt, pes):

    pokemons = db.samples_pokemon.find()

    for pokemon in pokemons:
        if nom == pokemon['name']:
            return jsonify({'error': 'Already Exists'}), 403
        
    nombre = nom
    tipo = tip
    altura = alt
    peso = pes
    id = ObjectId()
    idPKMN = sigID()
    numero = sigNum()

    nuevoPkmn = { "_id": id, "id": idPKMN, "name": nombre , "type": tipo, "num": numero, "height": altura, "weight": peso }
    db['samples_pokemon'].insert_one(nuevoPkmn)

    return jsonify({
        'id':       str(id),    # pasa a string el ObjectId
        'nombre':   nombre, 
        'tipo':     tipo,
        'numero':   numero
    })

def actualizarPut(nom, num, tip, alt, pes, id):
    pokemons = db.samples_pokemon.find()

    for pokemon in pokemons:
        if nom == pokemon['name']:
            return jsonify({'error': 'Already Exists'}), 403
            
    try:
        pokemon = db['samples_pokemon'].find_one({'_id':ObjectId(id)})
        nombre = nom
        numero = num
        tipo = tip
        altura = alt
        peso = pes
        

        if numero == '':
            numero = pokemon.get('num')

        if tipo == '':
            tipo = pokemon.get('type')

        if nombre == '':
            nombre = pokemon.get('name')
                
        if altura == '':
            altura = pokemon.get('height')

        if peso == '':
            peso = pokemon.get('weight')

        pkmnEdit = { "$set": { "name": nombre , "type": tipo, "num": numero, "height": altura, "weight": peso } }
        pkmn = { "_id": ObjectId(id) }

        db['samples_pokemon'].update_one(pkmn, pkmnEdit)

        pokemon = db['samples_pokemon'].find_one({'_id': ObjectId(id)})

        return jsonify({
            'id':       id,
            'nombre':   pokemon.get('name'),
            'tipo':     pokemon.get('type'),
            'numero':   pokemon.get('num')
        })

    except:
        return jsonify({'error': 'Not Found'}), 404

def eliminarDelete(id):
    try:
        pokemon = db['samples_pokemon'].find_one({'_id': ObjectId(id)})

        db['samples_pokemon'].delete_one({ "_id": ObjectId(id) })

        return jsonify({
            'id':   id
        })

    except:
        return jsonify({'error': 'Not Found'}), 404

def getLista():
    return lista_pokemon