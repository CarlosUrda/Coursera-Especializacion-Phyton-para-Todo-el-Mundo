#!/usr/bin/env python
#coding=utf-8

# Lectura de una web indicada por el usuario usando sockets. El contenido de
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

print "Petición GET enviada correctamente a", url, "\n"

maxTamannoBloque = 284
tamannoBloque = 0
bloque = 1 
datos = None

# En este bucle evitamos tener que llamar varias veces a recv, porque cuando
# al recibir datos sobrepasa el tamaño máximo del bloque, en la siguiente
# iteración se procesan esos datos sobrantes hasta que ya no se sobrepasa el
# tamaño máximo, que es cuando se vuelve a leer.
while True:
    # Si no hay datos pendientes que sobraron del bloque anterior.
    if datos is None:
        datos = sock.recv(1024)
        tamanno = len( datos)
        if tamanno < 1: break
        tamannoBloque += tamanno
    
    if tamannoBloque <= maxTamannoBloque:
        print datos
        datos = None
        continue

    tamannoBloque -= maxTamannoBloque 
    print datos[:-tamannoBloque]
    raw_input( "\n*** Fin de Bloque " + str( bloque) + " --> " +\
               str( maxTamannoBloque) + " CARACTERES ***")
    bloque += 1
    datos = datos[-tamannoBloque:]

print "Tamaño total: ", (bloque-1)*maxTamannoBloque + tamannoBloque

