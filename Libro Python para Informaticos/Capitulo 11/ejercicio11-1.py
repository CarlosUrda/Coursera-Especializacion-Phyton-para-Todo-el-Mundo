#!/usr/bin/env python
#coding=utf-8

# Simulación del comando grep de UNIX. Cuenta el número de líneas que coinciden 
# con la expresión regular.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "10/01/2016"


import re

while True:
    nombreDeArchivo = raw_input( "Introduce el archivo: ")
    if not nombreDeArchivo: continue
    
    try:
        archivo = open( nombreDeArchivo)
    except:
        print "El archivo no existe."
        continue
    break

expresion = raw_input( "Introduce la expresión regular: ")

cuentaLineas = 0

for linea in archivo:
    if re.search( expresion, linea) != None:
        cuentaLineas += 1

print "El archivo", nombreDeArchivo, "tiene", cuentaLineas, \
      "lineas que coinciden con", expresion
