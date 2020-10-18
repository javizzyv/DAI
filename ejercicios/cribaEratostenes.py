def isPrimo (numero):
    seguir = True
    divisor = numero - 1

    while(seguir and divisor > 1):
        if (numero % divisor == 0):
            seguir = False
        else:
            divisor = divisor - 1
    
    return seguir

numero = int(input('Introduce un numero natural para aplicarle la criba de Eratostenes: '))

if numero > 0:
    for i in range(numero-1,0,-1):
        if(isPrimo(i)):
            print(str(i) + ' ')
if (numero < 0):
    print('El número que ha introducido es negativo.')
if (numero == 0):
    print('El numero que ha introducido es 0, no hay ningun natural menor')
