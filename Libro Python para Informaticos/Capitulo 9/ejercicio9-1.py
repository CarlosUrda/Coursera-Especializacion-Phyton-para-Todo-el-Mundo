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


while True:
    nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")
    if not nombreDeArchivo: continue
 
    try:
       archivo = open( nombreDeArchivo)
    except:
        print "El archivo no existe"
        continue

    break

diccionario = {}
for palabra in archivo:
    palabra = palabra.strip()
    existePalabra = diccionario.has_key( palabra)
    diccionario[palabra] = 1 if not existePalabra else diccionario[palabra]+1

archivo.close()
print diccionario


