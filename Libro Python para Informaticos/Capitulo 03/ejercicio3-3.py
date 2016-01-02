#coding=utf-8

puntuacion = raw_input( "Introduce la puntuación: ")

try:
    puntuacion = float( puntuacion)
except:
    print "Tienes que introducir un número"
    quit()

if puntuacion < 0.0 or puntuacion > 1:
    print "Tienes que introducir un número en el rango [0,1]"
elif puntuacion >= 0.9:
    print "Sobresaliente"
elif puntuacion >= 0.8:
    print "Notable"
elif puntuacion >= 0.7:
    print "Bien"
elif puntuacion >= 0.6:
    print "Suficiente"
else:
    print "Insuficiente"
      
