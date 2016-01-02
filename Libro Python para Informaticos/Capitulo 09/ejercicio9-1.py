#!/usr/bin/env python
#coding=utf-8

# Extraer todas las palabras de un archivo y guardarlas como claves en un 
# diccionario junto con el número de veces que aparece.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "26/12/2015"


while True:
    nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")
    if not nombreDeArchivo: continue
 
    try:
       archivo = open( nombreDeArchivo)
    except:
        print "El archivo no existe"
        continue

    break

palabras = {}
for palabra in archivo:
    palabra = palabra.strip()
    palabras[palabra] = palabras.get( palabra, 0) + 1

archivo.close()
print palabras


