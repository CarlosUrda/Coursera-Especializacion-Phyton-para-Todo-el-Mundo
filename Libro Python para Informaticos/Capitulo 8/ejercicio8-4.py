#!/usr/bin/env python
#coding=utf-8

# Extraer todas las palabras de un archivo y mostrarlas de manera ordenada en
# una lista.

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

ordenadas = []

[ordenadas.append( palabra) for linea in archivo for palabra in linea.split() 
                                                 if palabra not in ordenadas] 

#for linea in archivo:
#    palabras = linea.split()
#    [ordenadas.append( palabra) for palabra in palabras 
#                                    if palabra not in ordenadas]

ordenadas.sort()
print ordenadas

archivo.close()
