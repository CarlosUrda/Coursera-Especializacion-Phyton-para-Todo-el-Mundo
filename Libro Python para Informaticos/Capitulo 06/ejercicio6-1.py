#!/usr/bin/env python
#coding=utf-8

# Mostrar cada carácter de una cadena en una líena empezando por el final de
# la cadena.

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

i = len( cadena) - 1
while i >= 0:
    print cadena[i]
    i -= 1

