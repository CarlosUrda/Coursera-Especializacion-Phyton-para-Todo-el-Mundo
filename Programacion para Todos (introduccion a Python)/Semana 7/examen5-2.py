#!/usr/bin/env python
#coding=utf-8

# Programa que solicita números al usuario hasta que introduce la palabra 
# «done», en cuyo caso muestra el máximo y el mínimo de los números metidos.
# Si se introduce un valor que no es un número mostrar el mensaje de error 
# «Invalid input».

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "17/12/2015"


maximo = None
minimo = None
while True:
    numero = raw_input( "Introduce un número: ")
    if numero.lower() == "done":
        break

    try:
        numero = int( numero)
    except:
        print "Invalid input"
        continue

    if maximo is None:
        maximo = minimo = numero
    elif maximo < numero:
        maximo = numero
    elif minimo > numero:
        minimo = numero

print "Maximum is " + str( maximo)
print "Minimum is " + str( minimo)


