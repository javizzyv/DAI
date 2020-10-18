import random
from time import time

def inicializarVector ():
    vector = []
    for _ in range(10):
        vector.append(random.randrange(1,50))
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
print('Vector original(Burbuja): ' + str(vectorB))
t1B = time()
burbuja(vectorB)
t2B = time()

vectorS = inicializarVector()
print('Vector original(Seleccion): ' + str(vectorS))
t1S = time()
seleccion(vectorS)
t2S = time()

vectorI = inicializarVector()
print('Vector original(Insercion): ' + str(vectorI))
t1I = time()
insercion(vectorI)
t2I = time()

print('\n')

print('Ordenado(Burbuja): ' + str(vectorB))
print('Ordenado(Seleccion): ' + str(vectorS))
print('Ordenado(Insercion): ' + str(vectorI))

print('\n')

print('Tiempo que ha tardado (Burbuja): ' + str(t2B-t1B))
print('Tiempo que ha tardado (Seleccion): ' + str(t2S-t1S))
print('Tiempo que ha tardado (Insercion): ' + str(t2I-t1I))