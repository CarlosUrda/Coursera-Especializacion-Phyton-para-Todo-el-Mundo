#!/usr/bin/env python
#coding=utf-8

# Contar el número de párrafos <p> en un documento html.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "25/01/2016"


import bs4
import re
import urllib

regex = "^http://(\w(-*\w)*(\.\w(-*\w)*)+)(/[^/\s]+)*$"
 
while True:
    url = raw_input( "Introduce la dirección url: ").strip()
    if not url: continue

    if re.match( regex, url) is not None: break

    print "Formato de url incorrecto."
    continue


print "Formato de url válido:", url

try:
    urlAbierta = urllib.urlopen( url)
except:
    print "ERROR: No se ha podido acceder a la dirección url."
    exit()

docHtml = urlAbierta.read()
sopa = bs4.BeautifulSoup( docHtml)

print "El número de párrafos <p> es:", len( sopa('p'))

    


