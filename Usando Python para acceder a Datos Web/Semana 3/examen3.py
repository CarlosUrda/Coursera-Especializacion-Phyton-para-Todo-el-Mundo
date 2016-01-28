#!/usr/bin/env python
#coding=utf-8

# Examen de la Semana 3 del Curso 3. Obtener las cabeceras de una web.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "27/01/2016"


import socket
import re

regex = "^(http://(\w(-*\w)*(\.\w(-*\w)*)+)(/[^/\s]+)*):(?P<puerto>\d+)$"
 
while True:
    direccion = raw_input( "Introduce dirección «url:puerto» => ").strip()
    match = re.search( regex, direccion)

    if match is not None:
        url = match.group(1)
        servidor = match.group(2)
        puerto = int( match.groupdict()['puerto'])
        break

    print "Formato de URL incorrecto."

print "Formato de url", match.group(0), "válido"

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect( (servidor, puerto))
except:
    print "Error al crear conexión con servidor", servidor, "en puerto", puerto
    exit()

print "Conexión realizada con", servidor, "en el puerto", puerto

try:
    sock.send( "GET " + url + " HTTP/1.0\n\n")
except:
    print "Error al enviar la petición GET a", url
    exit()

print "Petición GET enviada correctamente a", url, "\n"

while True:
    datos = sock.recv(1024)
    tamanno = len( datos)
    if tamanno < 1: break

    print datos
