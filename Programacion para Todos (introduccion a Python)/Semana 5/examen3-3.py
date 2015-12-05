puntuacion = raw_input( "Introduce la puntuacion: ")
try:
    puntuacion = float( puntuacion)
except:
    print( "Introduce un numero")
    quit()

if puntuacion < 0 or puntuacion > 1:
    print "El numero introducido esta fuera del rango [0,1]"
elif puntuacion >= 0.9:
    print "A"
elif puntuacion >= 0.8:
    print "B"
elif puntuacion >= 0.7:
    print "C"
elif puntuacion >= 0.6:
    print "D"
else:
    print "F"

