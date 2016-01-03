#!/usr/bin/env python
#coding=utf-8

# Mostrar la frecuencia de las letras en un archivo.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "03/01/2016"


import string

while True:
    nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")
    if not nombreDeArchivo: continue

    try:
        archivo = open( nombreDeArchivo)
    except:
        print "¡El archivo no existe!"
        continue

    break

cuentaLetras = dict()
tabla = zip( u"áéíóú" + unicode( string.punctuation), 
             list(u"aeiou") + [None]*len( string.punctuation))
tabla = {ord(ini):(ord(fin) if fin else None) for ini,fin in tabla}
print tabla

for linea in archivo:
    linea = unicode( linea)
    linea = linea.lower().translate( tabla)

    linea = linea.encode()
    for letra in linea:
        cuentaLetras[letra] = cuentaLetras.get( letra, 0) + 1

ordenLetras = []
for letra, cuenta in cuentaLetras.items():
    ordenLetras.append( (cuenta, letra))

ordenLetras.sort( reverse=True)

for cuenta, letra in ordenLetras:
    print letra, cuenta

print string.punctuation
