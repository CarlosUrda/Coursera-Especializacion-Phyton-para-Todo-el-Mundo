#!/usr/bin/env python
#coding=utf-8

# Examen de la Semana 1 del Curso 2.
# Extraer un número de la cadena,

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2015"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "18/12/2015"


text = "X-DSPAM-Confidence:    0.8475"

numero = float( text[text.find( ":")+1:].strip())                            
print numero 
