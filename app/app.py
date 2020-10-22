#./app/app.py
from flask import Flask
from flask import request
from flask import Response
app = Flask(__name__)


@app.route('/')

def index():
    return '<a href="static/index.html"><h3> Pincha para ir a la página principal </h3></a>'


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


@app.errorhandler(404)

def page_not_found(error):
    return "404 Not Found", 404