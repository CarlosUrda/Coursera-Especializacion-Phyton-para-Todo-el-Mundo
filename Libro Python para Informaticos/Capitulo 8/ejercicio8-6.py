#!/usr/bin/env python
#coding=utf-8

# Mostrar el máximo y el mínimo de los números introducidos.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "26/12/2015"


numeros = []

while True:
    numero = raw_input( "Introduce un número: ")
    if not numero: continue
    if numero.lower() == "fin": break
    try:
        numero = float( numero)
    except:
        print "¡Tienes que introducir un número!"
        continue

    numeros.append( numero)

# Operador ternario: -- a if comp else b --
print "Máximo:", max( numeros) if numeros else "Ninguno"
print "Mínimo:", min( numeros) if numeros else "Ninguno"
print "Número de números:", len( numeros)

