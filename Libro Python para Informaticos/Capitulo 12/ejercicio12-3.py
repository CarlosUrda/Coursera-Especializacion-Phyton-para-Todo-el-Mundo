#!/usr/bin/env python
#coding=utf-8

# Lectura de una web indicada por el usuario usando urllib. El contenido de
# la página se muestra por bloques.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "16/01/2016"


import urllib
import re

while True:
    direccion = raw_input( "Introduce dirección url => ").strip()
    regex = "^http://(\w(-*\w)*(\.\w(-*\w)*)+)(/[^/\s]+)*"
    match = re.search( regex, direccion)

    if match is not None:
        url = match.group(0)
        break

    print "Formato de URL incorrecto."

print "Formato de url", url, "válido."

try:
    urlAbierta = urllib.urlopen( url)
except:
    print "Error al abrir la dirección", url, "."
    exit()

print "Dirección", url, "abierta correctamente.\n"

maxTamannoBloque = 1167
tamannoBloque = 0
bloque = 1 
datos = ""

# En este bucle se reduce un poco el código respecto al ejercicio 2 pero a 
# costa de llamar varias veces a read aun habiendo llegado al final de los
# datos del archivo de entrada. Esto sucede cuando los últimos datos leídos
# hacen sobrepasar el tamaño máximo del bloque y los datos restantes se 
# procesan en las siguientes iteraciones pero ya no quedan datos por leer del
# archivo de entrada.
while True:
    datos += urlAbierta.read(1024)
    tamanno = len( datos)

    if tamanno < 1: break

    tamannoBloque += tamanno
    if tamannoBloque <= maxTamannoBloque:
        print datos
        datos = ""
        continue

    tamannoRestante = tamannoBloque - maxTamannoBloque 
    print datos[:-tamannoRestante] 
    raw_input( "\n*** Fin de Bloque " + str( bloque) + " --> " +\
               str( maxTamannoBloque) + " CARACTERES ***")
    bloque += 1
    datos = datos[-tamannoRestante:]
    tamannoBloque = 0

print "Tamaño total: ", (bloque-1)*maxTamannoBloque + tamannoBloque
