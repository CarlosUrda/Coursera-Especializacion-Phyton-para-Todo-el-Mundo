#!/usr/bin/env python
#coding=utf-8

# Introducir una serie de números por teclado y obtener la suma, máximo y 
# mínimo de todos ellos.

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
maximo = None
minimo = None


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
    if maximo is None or numero > maximo:
        maximo = numero
    if minimo is None or numero < minimo:
        minimo = numero

    numeroDeNumeros += 1

print "Total de números: " + str( numeroDeNumeros)
print "Suma total: " + str( sumaTotal)
print "Máximo: " + str( maximo)
print "Mínimo: " + str( minimo)




