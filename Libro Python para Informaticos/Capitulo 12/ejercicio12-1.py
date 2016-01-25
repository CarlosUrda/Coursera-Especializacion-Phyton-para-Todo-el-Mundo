#!/usr/bin/env python
#coding=utf-8

# Lectura de una web indicada por el usuario usando sockets. 

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "16/01/2016"


import socket
import re

regex = "^http://(\w(-*\w)*(\.\w(-*\w)*)+)(/[^/\s]+)*:(\d+)$"
 
while True:
    direccion = raw_input( "Introduce dirección «url:puerto» => ").strip()
    match = re.search( regex, direccion)

    if match is not None:
        servidor = match.group(1)
        url_puerto = match.group(0).rsplit(":", 1)
        url = url_puerto[0]
        puerto = int( url_puerto[1])
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

print "Petición GET enviada correctamente a", url

while True:
    datos = sock.recv(1024)
    if len( datos) < 1: break

    print datos
