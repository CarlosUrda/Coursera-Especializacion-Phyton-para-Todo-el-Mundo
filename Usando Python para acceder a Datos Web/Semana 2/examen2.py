#!/usr/bin/env python
#coding=utf-8

# Examen de Semana 2: Buscar líneas que tengan numeros, extrayendo su valor y 
# calculando la suma total de todos ellos.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "11/01/2016"


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

expresion = "[\d]+\.?[\d]*"
cuentaValores = 0
cuentaLineas = 0
total = 0

for linea in archivo:
    linea = linea.strip()
    valores = re.findall( expresion, linea)
    if not valores: continue

    cuentaLineas += 1
    cuentaValores += len( valores)
    total += sum([float(valor) for valor in valores])

print "El archivo", nombreDeArchivo, "tiene", cuentaLineas, \
      "lineas y", cuentaValores, "valores que coinciden con", expresion
print "La suma de todos los valores es %f" % total     
