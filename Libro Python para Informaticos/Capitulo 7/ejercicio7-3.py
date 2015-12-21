#!/usr/bin/env python
#coding=utf-8

# Encontrar todas las líneas de un archivo que empiezan con un formato X-DSPAM
# y mostrar el valor medio encontrado en esas líneas. 

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "21/12/2015"


nombreDeArchivo = raw_input( "Introduce el nombre del archivo: ")

if nombreDeArchivo.lower() == "na na boo boo":
    print "NA NA BOO BOO PARA TI - ¡Te he pillado!"
    exit()

try:
    archivo = open( nombreDeArchivo)
except:
    print "El archivo no existe"
    quit()

cuentaSpam = 0
valorSpam = 0
for linea in archivo:
    if not( linea.upper().startswith( "X-DSPAM-CONFIDENCE:")): continue

    try:
        valorSpam += float( linea[linea.find( ":")+1:])
    except:
        continue

    cuentaSpam += 1

print "Número de líneas encontradas: " + str( cuentaSpam)
print "Valor medio: " + str( valorSpam / cuentaSpam)


