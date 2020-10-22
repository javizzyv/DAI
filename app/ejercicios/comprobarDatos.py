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
  

dato = input('Introduce el dato: ')
  
if nombre(dato):
    print ("Es un nombre")

if email(dato):
    print ("Es un email")
    
if tarjeta(dato):
    print ("Es un numero de tarjeta")