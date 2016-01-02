#!/usr/bin/env python
#coding=utf-8

# Monstrar los emisores y el número de estos obtenidos de un archivo buzón.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "26/12/2015"


nombreDeArchivo = raw_input( "Introduce el archivo: ")
try:
    archivo = open( nombreDeArchivo)
except:
    print "No existe el archivo", nombreDeArchivo
    quit()

emisores = []

for linea in archivo:
    palabras = linea.split()
    if len( palabras) < 2 or palabras[0].upper() != "FROM" or not palabras[1]:
        continue
    emisores.append( palabras[1])

for emisor in emisores: print emisor
print "Hay", len( emisores), "líneas con From y emisor"

archivo.close()
