#!/usr/bin/env python
#coding=utf-8

# Mostrar la dirección de correo que tiene más mensajes enviados en un registro
# de correos.

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

cuentaDeCorreos = dict()
correoMasFrecuente = None

for linea in archivo:
    palabras = linea.split()

    if len( palabras) < 2 or palabras[0].upper() != "FROM":
        continue

    correo = palabras[1]
    cuentaDeCorreos[correo] = cuentaDeCorreos.get( correo, 0) + 1

    if (correoMasFrecuente is None or 
        cuentaDeCorreos[correo] > cuentaDeCorreos[correoMasFrecuente]):
        correoMasFrecuente = correo
       
print correoMasFrecuente, cuentaDeCorreos[correoMasFrecuente]


