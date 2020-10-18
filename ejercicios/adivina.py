import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

número = random.randint(1, 100)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 100.')

while intentosRealizados < 11:
    print('Intenta adivinar.')
    estimación = input()
    estimación = int(estimación)
    intentosRealizados = intentosRealizados + 1
    if estimación < número:
        print('Tu estimación es muy baja.')
    if estimación > número:
        print('Tu estimación es muy alta.')
    if estimación == número:
        break

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

if estimación != número:
    número = str(número)
    print('Pues no. El número que estaba pensando era ' + número)