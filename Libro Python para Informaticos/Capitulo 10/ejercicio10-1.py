#!/usr/bin/env python
#coding=utf-8

# Mostrar la dirección de correo que tiene más mensajes enviados en un registros
# de correos.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "02/01/2016"


while True:
    nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")
    if not nombreDeArchivo: continue

    try:
        archivo = open( nombreDeArchivo)
    except:
        print "¡El archivo no existe!"
        continue

    break

cuentaCorreos = dict()

for linea in archivo:
    palabras = linea.split()

    if len( palabras) < 2 or palabras[0].upper() != "FROM":
        continue

    correo = palabras[1]
    cuentaCorreos[correo] = cuentaCorreos.get( correo, 0) + 1

ordenCorreos = []
for correo, cuenta in cuentaCorreos.items():
    ordenCorreos.append( (cuenta, correo))

ordenCorreos.sort( reverse=True)

cuenta, correo = ordenCorreos[0]
print correo, cuenta


