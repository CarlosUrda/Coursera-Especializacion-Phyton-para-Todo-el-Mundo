#!/usr/bin/env python
#coding=utf-8

# Introducir una serie de números por teclado y obtener la suma y media de
# ellos.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "16/12/2015"


sumaTotal = 0
numeroDeNumeros = 0
while True:
    numero = raw_input( "Introduce un número: ")
    if numero.lower() == "fin":
        break

    try:
        numero = float( numero)
    except:
        print "Debes introducir un número"
        continue

    sumaTotal += numero
    numeroDeNumeros += 1

print "Total de números: " + str( numeroDeNumeros)
print "Suma total: " + str( sumaTotal)
print "Media: " + str( sumaTotal*1. / numeroDeNumeros)




