#!/usr/bin/env python
#coding=utf-8

#  Contar el número de apariciones de una letra en una cadena.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "18/12/2015"


cadena = raw_input(  "Introduce una cadena: ")
letra = raw_input( "Introduce una letra: ")
print "Número de apariciones: " + str( cadena.count( letra))

