#!/usr/bin/env python
#coding=utf-8

# Examen 2 de la Semana 4 del Curso 3. Buscar a través de los enlaces de una 
# página web.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "06/02/2016"

import bs4, urllib, ssl, json

def leerValor( mensajeEntrada, cambiarValor, mensajeErrorCambiarValor, 
               comprobarValor, mensajeErrorComprobarValor):
    while True:
        valor = raw_input( mensajeEntrada).strip()
        if not valor: continue
        try:
            valor = cambiarValor( valor)
        except:
            print mensajeErrorCambiarValor

        if comprobarValor( valor): break
        print mensajeErrorComprobarValor

    return valor


while True:
    url = raw_input( "Introduce la web: ").strip()
    if url: break

posicion = leerValor( "Posición relativa del enlace a entrar: ", int,
                      "Introduce un número entero",  lambda x: x > 0,
                      "Introduce una posición positiva > 0")
iteraciones = leerValor( "Veces que se repite el proceso: ", int, 
                         "Introduce un número entero", lambda x: x >= 0,
                         "Introduce una iteración positiva => 0")

contexto = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

for i in range( iteraciones):
    try:
        web = urllib.urlopen( url, context=contexto)
    except:
        print "La dirección web %s no es correcta." % direccionWeb
        exit()

    print "Obteniendo enlaces de... %s" % url
    sopa = bs4.BeautifulSoup( web.read(), 'html.parser')
    enlaces = sopa.find_all( "a")
    if len( enlaces) < posicion: 
        print( "En la web %s no hay suficientes enlaces." % url)
        exit()

    url = enlaces[posicion-1].get( "href")
    if url is None:
        print( "El enlace %s no tiene atributo href" % url)
        exit()

print "Final => ", url

