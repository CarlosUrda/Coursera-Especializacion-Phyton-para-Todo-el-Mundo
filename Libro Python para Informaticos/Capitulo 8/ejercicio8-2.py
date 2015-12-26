#!/usr/bin/env python
#coding=utf-8

# Mostrar el día de la semana del archivo con formatos correos electrónicos.
# Mejorar el código para solucionar todos los posible casos de error. 

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

for linea in archivo:
    palabras = linea.split()
    if len( palabras) < 3 or palabras[0] != 'From' or not palabras[2]:
        continue
    print palabras[2]

archivo.close()
