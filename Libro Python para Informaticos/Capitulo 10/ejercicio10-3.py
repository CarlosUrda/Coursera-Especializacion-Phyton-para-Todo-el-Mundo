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

# tablala a usar como mapeo en la traducción de cada línea.
cuentaLetras = dict()
letrasACambiar = [ord(letra) for letra in u"áéíóú"]
letrasCambiadas = [ord(letra) for letra in u"aeiou"]
letrasABorrar = [ord(letra) for letra in unicode(string.punctuation + " \n\t\r"+
                                                 string.digits, 'utf-8')]
tabla = dict( zip( letrasACambiar + letrasABorrar, letrasCambiadas +
                   [None]*len(letrasABorrar)))

for linea in archivo:
    linea = unicode( linea, 'utf-8')
    linea = linea.lower().translate( tabla)

    for letra in linea:
        cuentaLetras[letra] = cuentaLetras.get( letra, 0) + 1

ordenLetras = []
for letra, cuenta in cuentaLetras.items():
    ordenLetras.append( (cuenta, letra))

ordenLetras.sort( reverse=True)

for cuenta, letra in ordenLetras:
    print letra, cuenta

