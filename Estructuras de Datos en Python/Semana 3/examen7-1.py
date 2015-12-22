#!/usr/bin/env python
#coding=utf-8

# Examen 1 de la Semana 3 del Curso 2.
# Mostrar por pantalla el contenido de un archivo pasado a mayúsculas.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "22/12/2015"


nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")

try:
    archivo = open( nombreDeArchivo)
except:
    print "No se puede abrir el archivo", nombreDeArchivo
    quit()

for linea in archivo:
    print linea.rstrip().upper()
