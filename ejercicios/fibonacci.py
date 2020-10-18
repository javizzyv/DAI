import os

def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

archivoEntrada = 'ejercicios/entradaFibonacci.txt'
archivoSalida = 'ejercicios/resultadoFibonacci.txt'

with open(archivoEntrada) as f:
    numero = int(f.read())

print('El numero es: ' + str(numero))
print('\n')

resultado = Fibonacci(numero)

with open(archivoSalida, 'w') as f:
    f.write(str(resultado))

print('El resultado de Fibonacci para ' + str(numero) + ' es ' + str(resultado))