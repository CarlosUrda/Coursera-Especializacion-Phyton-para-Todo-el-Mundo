#!/usr/bin/env python
#coding=utf-8

# Implementar las funciones recorta y centro. 
# Recorta: Eliminar el primer y último elemento de una lista.
# Centro: Devolver todos los elementos de una lista excepto el primero y el 
# último
__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "25/12/2015"



def recorta( lista):
    del lista[0:1]
    del lista[-1:]
    return None

def centro( lista):
    return lista[1:-1]


listas = [range( 10), [], [3]]
for lista in listas:
    print "Lista antes de recorta: ", lista
    print "Recorta:", recorta( lista)
    print "Lista después de recorta: ", lista

    print "Lista antes de centro: ", lista
    print "Centro:", centro( lista)
    print "Lista después de centro: ", lista
