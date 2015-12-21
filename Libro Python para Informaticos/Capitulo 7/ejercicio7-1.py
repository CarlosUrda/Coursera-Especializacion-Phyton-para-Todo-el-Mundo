#!/usr/bin/env python
#coding=utf-8

# Abrir un archivo e ir mostrando por pantalla y en mayúsculas cada una de las 
# líneas que lo componen.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "20/12/2015"


import sys

nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")

try:
    manejadorDeArchivo = open( nombreDeArchivo)
except:
    print "El archivo " + nombreDeArchivo + " no existe"
    sys.exit()

for linea in manejadorDeArchivo:
    print linea.upper().rstrip()

manejadorDeArchivo.close()

