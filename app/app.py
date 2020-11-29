#./app/app.py
from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from model import *
from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client.SampleCollections

app = Flask(__name__)

visitadas = []

app.secret_key = 'super secret key'

visitadas.append('index')
visitadas.append('ejercicio1')
visitadas.append('login')

@app.route('/')

def index():
    return render_template('index.html', visitadas=visitadas, usuarioActual=session['usuarioActual'])


@app.route('/index')

def inicio():
    return render_template('index.html', visitadas=visitadas, usuarioActual=session['usuarioActual'])



@app.route('/mongo', methods=['GET', 'POST'])

def mongo():
    error = None
    lista_pokemon = []

    if request.method == 'POST':

        if 'Tipo' in request.form and 'Nombre' in request.form:
            id = 0.0
            numero = 0
            pokemons = db.samples_pokemon.find()
            nombre = request.form['Nombre']
            tipo = request.form['Tipo']
            altura = request.form['Altura']
            peso = request.form['Peso']
            imagen = request.form['Imagen']
	

            for pokemon in pokemons:
                if nombre == pokemon['name']:
                    error = 'Already exists'
                    return render_template('buscarBD.html', error=error, pokemons=lista_pokemon, visitadas=visitadas)
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

            return render_template('lista.html', pokemons=lista_pokemon, visitadas=visitadas)


        if 'NombreBorrar' in request.form:
                pokemons = db.samples_pokemon.find()
                nombre = request.form['NombreBorrar']
        
                for pokemon in pokemons:
                    if nombre in pokemon['name']:
                        db['samples_pokemon'].delete_one(pokemon)
                        return render_template('buscarBD.html', pokemons=lista_pokemon, visitadas=visitadas)
                
                error = 'Not exists'
                return render_template('buscarBD.html', error=error, pokemons=lista_pokemon, visitadas=visitadas)

        
        if 'NombreEditar' in request.form:
                pokemons = db.samples_pokemon.find()
                nombre = request.form['NombreEditar']

                for pokemon in pokemons:
                    if nombre in pokemon['name']:
                        if not request.form['NuevoNombreEditar'] == '':
                            nombre = request.form['NuevoNombreEditar']
                        else:
                            nombre = pokemon['name']

                        if not request.form['TipoEditar'] == '':
                            tipo = request.form['TipoEditar']
                        else:
                            tipo = pokemon['type']

                        if not request.form['AlturaEditar'] == '':
                            altura = request.form['AlturaEditar']
                        else:
                            altura = pokemon['height']

                        if not request.form['PesoEditar'] == '':
                            peso = request.form['PesoEditar']
                        else:
                            peso = pokemon['weight']
                        
                        if not request.form['ImagenEditar'] == '':
                            imagen = request.form['ImagenEditar']
                        else:
                            imagen = pokemon['img']

                        editarPKM = { "$set": { "id": pokemon['id'], "num": pokemon['num'], "name": nombre, "img": imagen, "type": tipo, "height": altura, "weight": peso } }
                        db['samples_pokemon'].update_one(pokemon, editarPKM)
                        
                        return render_template('buscarBD.html', pokemons=lista_pokemon, visitadas=visitadas)
                
                error = 'Not exists'
                return render_template('buscarBD.html', error=error, pokemons=lista_pokemon, visitadas=visitadas)
                

        if 'Nombre' in request.form:
            nombre = request.form['Nombre']
            pokemons = db.samples_pokemon.find()
	
            for pokemon in pokemons:
                if nombre in pokemon['name']:
                    lista_pokemon.append(pokemon)
            

        if 'Numero' in request.form:
            numero = request.form['Numero']
            pokemons = db.samples_pokemon.find()
	
            for pokemon in pokemons:
                if numero in pokemon['num']:
                    lista_pokemon.append(pokemon)

        if 'Tipo' in request.form:
            tipo = request.form['Tipo']
            pokemons = db.samples_pokemon.find()
	
            for pokemon in pokemons:
                if tipo in pokemon['type']:
                    lista_pokemon.append(pokemon)

        if len(lista_pokemon) > 0:
            return render_template('lista.html', pokemons=lista_pokemon, visitadas=visitadas)
        else:
            error = 'Not exists'

    return render_template('buscarBD.html', error=error, pokemons=lista_pokemon, visitadas=visitadas)



@app.route('/user/<username>')

def bienvenidaUsuario(username):
    return f'¡Bienvenido {username}!'


@app.route('/hola')

def hello_world():
    return 'Hello, World!'


@app.route('/corchetes')

def avisoCorchetes():
    return '<h3> En la URL, después de <corchetes> debes poner <corchetes>/numero de corchetes que quieres </h3>'


@app.route('/corchetes/<secuencia>')

def corchetes(secuencia):
    import random

    def comprobar(miCadena): 
        bracket = ['[]'] 
        while any(x in miCadena for x in bracket): 
            for br in bracket: 
                miCadena = miCadena.replace(br, '') 
        return not miCadena 

    tamanioCadena = int(secuencia)
    cadena = ''

    for i in range(tamanioCadena):
        if(random.randint(0,1) == 0):
            cadena += '['
        else:
            cadena += ']'

    

    if (comprobar(cadena)):
        return '<h1> La cadena generada es: ' + cadena + '</h1>' + '<h2> Es una cadena balanceada. </h2>'
    else:
        return '<h1> La cadena generada es: ' + cadena + '<h2> No es una cadena balanceada. </h2>'


@app.route('/ordena')

def avisoOrdena():
    return '<h3> En la URL, después de <ordena> debes poner <ordena>/vector que quieres ordenar ej: 1,2,3,4 </h3>'


@app.route('/ordena/<vectorO>')

def ordena(vectorO):

    import random
    from time import time

    respuesta = ''

    def inicializarVector ():
        vector = vectorO.split(',')
        return vector

    def burbuja (listaVector):
        for i in range(len(listaVector)-1,0,-1):
            for j in range(i):
                if listaVector[j]>listaVector[j+1]:
                    aux = listaVector[j]
                    listaVector[j] = listaVector[j+1]
                    listaVector[j+1] = aux


    def seleccion (listaVectorS):
        for i in range(len(listaVectorS)):
            minimo = i
            for j in range(i,len(listaVectorS)):
                if (listaVectorS[j]<listaVectorS[minimo]):
                    minimo = j
            if (minimo != i):
                temp = listaVectorS[i]
                listaVectorS[i] = listaVectorS[minimo]
                listaVectorS[minimo] = temp

    def insercion (listaVectorI):
        for i in range (len(listaVectorI)):
            for j in range (i,0,-1):
                if (listaVectorI[j-1] > listaVectorI[j]):
                    temp = listaVectorI[j]
                    listaVectorI[j] = listaVectorI[j-1]
                    listaVectorI[j-1] = temp

    vectorB = inicializarVector()
    respuesta += '<h1> Vector original: ' + str(vectorB) + ' </h1>'
    t1B = time()
    burbuja(vectorB)
    t2B = time()

    vectorS = inicializarVector()
    t1S = time()
    seleccion(vectorS)
    t2S = time()

    vectorI = inicializarVector()
    t1I = time()
    insercion(vectorI)
    t2I = time()


    respuesta += '<h2> Ordenado(Burbuja): ' + str(vectorB) + ' </h2>'
    respuesta += '<h2> Ordenado(Seleccion): ' + str(vectorS) + ' </h2>'
    respuesta += '<h2> Ordenado(Insercion): ' + str(vectorI) + ' </h2>'

    respuesta += '<h3> Tiempo que ha tardado (Burbuja): ' + str(t2B-t1B) + ' </h3>'
    respuesta += '<h3> Tiempo que ha tardado (Seleccion): ' + str(t2S-t1S) + ' </h3>'
    respuesta += '<h3> Tiempo que ha tardado (Insercion): ' + str(t2I-t1I) + ' </h3>'

    return respuesta


@app.route('/fibonacci')

def avisoFibonacci():
    return '<h3> En la URL, después de <fibonacci> debes poner <fibonacci>/posicion en la sucesión </h3>'

@app.route('/fibonacci/<numeroF>')

def fibonacci(numeroF):
    import os

    resultadoF = ''

    def Fibonacci(n):
        if n<=0:
            return "Incorrect input"
        elif n==1:
            return 0
        elif n==2:
            return 1
        else:
            return Fibonacci(n-1)+Fibonacci(n-2)

    archivoSalida = 'resultadoFibonacci.txt'

    numero = int(numeroF)

    resultadoF += '<h1> El numero es: ' + str(numero) + '</h1>'

    resultado = Fibonacci(numero)

    with open(archivoSalida, 'w') as f:
        f.write(str(resultado))

    resultadoF += '<h2> El resultado de Fibonacci para ' + str(numero) + ' es ' + str(resultado) + '</h2>'
    return resultadoF


@app.route('/eratostenes')

def avisoEratostenes():
    return '<h3> En la URL, después de <eratostenes> debes poner <eratostenes>/número natural del que quieres que se haga el algoritmo </h3>'


@app.route('/eratostenes/<natural>')

def eratostenes(natural):

    resultado = '<h1> '

    def isPrimo (numero):
        seguir = True
        divisor = numero - 1

        while(seguir and divisor > 1):
            if (numero % divisor == 0):
                seguir = False
            else:
                divisor = divisor - 1
        
        return seguir

    numero = int(natural)

    if numero > 0:
        for i in range(numero-1,0,-1):
            if(isPrimo(i)):
                resultado += str(i) + ' '
    if (numero < 0):
        return '<h1> El número que ha introducido es negativo. </h1>'
    if (numero == 0):
        return '<h1> El numero que ha introducido es 0, no hay ningun natural menor. </h1>'

    resultado += ' </h1>'
    return resultado


@app.route('/comprobar')

def avisoDatos():
    return '<h3> En la URL, después de <comprobar> debes poner <comprobar>/el dato que quieras comprobar </h3>'


@app.route('/comprobar/<datos>')

def comprobar(datos):

    import re

    def nombre(string):
        datoN = re.compile(r'([A-Za-z]+) ([A-Z])')
        return datoN.match(string)


    def email(string):
        datoE = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b')
        return datoE.match(string)


    def tarjeta(string):
        datoT = re.compile(r'([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})')
        return datoT.match(string)
    

    dato = datos
    
    if nombre(dato):
        return '<h1> Es un nombre </h1>'

    else:
        if email(dato):
            return '<h1> Es un email </h1>'
        
        else :
            if tarjeta(dato):
                return '<h1> Es un numero de tarjeta </h1>'
            else:
                return '<h1> No es nada de eso o has introducido mal el dato </h1>'


@app.route('/svg')

def inicializarSVG ():
    import random

    colores = ['red','blue','green','purple','black','white','yellow']

    

    numFiguras = random.randint(1,20)

    resultado = ''

    for _ in range(0,numFiguras):
        figura = random.randint(1,2)

        alto = random.randint(50,200)
        ancho = random.randint(50,200)

        trazo = random.choice(colores)
        relleno = random.choice(colores)

        cx = random.randint(5,100)
        cy = random.randint(5,100)
        r = random.randint(10,20)

        x = random.randint(5,100)
        y = random.randint(5,100)
        rx = random.randint(10,20)
        ry = random.randint(10,20)

        if (figura == 1):
            resultado += '<svg width="350" height="350"><rect x=' + str(x) + ' y=' + str(y) + ' rx=' + str(rx) +  ' ry=' + str(ry) + ' width=' + str(ancho) + ' height=' + str(alto) + ' style="fill:' + str(relleno) +';stroke:' + str(trazo) + ';stroke-width:5;opacity:0.5" /></svg>'
        elif (figura == 2): 
            resultado += '<svg width="350" height="350"><circle cx=' + str(cx) + ' cy=' + str(cy) +  ' r=' + str(r) + ' style="fill:' + str(relleno) + ';stroke:' + str(trazo) + ';stroke-width="5";opacity:0.5" /></svg>'
    
    return resultado


@app.route('/login', methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['Username']
        contrasenia = request.form['Password']

        if loginPickle(usuario, contrasenia) == False:
            error = 'Invalid credentials'
        else:
            session['usuarioActual'] = usuario
            session['contraseniaActual'] = contrasenia
            usuarioActual = usuario
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error, visitadas=visitadas)


@app.route('/registrarse', methods=['GET', 'POST'])

def registrarse():
    error = None
    if request.method == 'POST':
        usuario = request.form['Username']
        contrasenia = request.form['Password']

        if registroPickle(usuario, contrasenia) == False:
            error = 'Nick already used'
        else:
            session['usuarioActual'] = usuario
            session['contraseniaActual'] = contrasenia
            usuarioActual = usuario
            flash('You were successfully sign in')
            return redirect(url_for('index'))
    return render_template('registrarse.html', error=error, visitadas=visitadas)

@app.route('/logout')

def logout():
    session['usuarioActual'] = 'anon'
    session['contraseniaActual'] = ''
    return redirect(url_for('index'))


@app.route('/ejercicio1', methods=['GET', 'POST'])

def ejercicio1():
    if request.method == 'POST':
        
        import random

        numero = random.randint(1, 10)


        estimacion = request.form['numeroAdivina']
        estimacion = int(estimacion)

        if estimacion == numero:
            cadena = '¡Buen trabajo! ¡Mi número es ' + str(numero) + '!'
            return render_template('enBlanco.html', visitadas=visitadas, contenido=cadena)

        if estimacion != numero:
            cadena = 'Pues no. El número que estaba pensando era ' + str(numero)
            return render_template('enBlanco.html', visitadas=visitadas, contenido=cadena)

    return render_template('ejercicio1.html', visitadas=visitadas)


@app.route('/editarUsuario', methods=['GET', 'POST'])

def editarU():
    error = None
    if request.method == 'POST':
        usuario = request.form['Username']
        contrasenia = request.form['Password']

        if editarPickle(usuario, contrasenia, session['usuarioActual']) == False:
            error = 'Nick already used'
        else:
            session['usuarioActual'] = usuario
            session['contraseniaActual'] = contrasenia
            usuarioActual = usuario
            flash('You were successfully changed your profile')
            return redirect(url_for('index'))
    return render_template('editarDatos.html', visitadas=visitadas, error=error, nombre=session['usuarioActual'], contrasenia=session['contraseniaActual'])


@app.route('/visualizarUsuario')

def visualizarU():
    return render_template('visualizarDatos.html', visitadas=visitadas, nombre=session['usuarioActual'], contrasenia=session['contraseniaActual'])

@app.errorhandler(404)

def page_not_found(error):
    return "404 Not Found", 404