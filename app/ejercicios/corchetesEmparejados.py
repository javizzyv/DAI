import random

def comprobar(miCadena): 
    bracket = ['[]'] 
    while any(x in miCadena for x in bracket): 
        for br in bracket: 
            miCadena = miCadena.replace(br, '') 
    return not miCadena 

tamanioCadena = int(input('Introduce el tamaño que quieres que tenga la cadena: '))
cadena = ''

for i in range(tamanioCadena):
    if(random.randint(0,1) == 0):
        cadena += '['
    else:
        cadena += ']'

print('\n')
print('La cadena es: ' + cadena)

if (comprobar(cadena)):
    print('Es una cadena balanceada.')
else:
    print('No es una cadena balanceada.')