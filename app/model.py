from pickleshare import *


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