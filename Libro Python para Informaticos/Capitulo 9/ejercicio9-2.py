#!/usr/bin/env python
#coding=utf-8

# Contar el número de mensajes de cada día de la semana en un registro de
# correos.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "30/12/2015"


while True:
    nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")
    if not nombreDeArchivo: continue

    try:
        archivo = open( nombreDeArchivo)
    except:
        print "¡El archivo no existe!"
        continue

    break

cuentaMensajes = dict()

for linea in archivo:
    palabras = linea.split()

    if len( palabras) < 3 or palabras[0].upper() != "FROM":
        continue

    dia = palabras[2].capitalize()
    cuentaMensajes[dia] = cuentaMensajes[dia]+1 if dia in cuentaMensajes else 1

print cuentaMensajes


