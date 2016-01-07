#!/usr/bin/env python
#coding=utf-8

# Examen de la Semana 10: Mostrar la frecuencia de las horas del día de los 
# mensajes enviados en un registros de correos.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "03/01/2016"


while True:
    nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")
    if not nombreDeArchivo: continue

    try:
        archivo = open( nombreDeArchivo)
    except:
        print "El archivo no existe!"
        continue

    break

cuentaHoras = dict()

for linea in archivo:
    palabras = linea.split()

    if len( palabras) < 6 or palabras[0].upper() != "FROM":
        continue

    hora = palabras[5][:2]
    cuentaHoras[hora] = cuentaHoras.get( hora, 0) + 1

ordenHoras = cuentaHoras.items()
ordenHoras.sort()
for hora, cuenta in ordenHoras:
    print hora, cuenta

