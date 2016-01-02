#coding=utf-8

def calcula_calificacion( puntuacion):
    if puntuacion < 0.0 or puntuacion > 1:
        return "Tienes que introducir un número en el rango [0,1]"
    elif puntuacion >= 0.9:
        return "Sobresaliente"
    elif puntuacion >= 0.8:
        return "Notable"
    elif puntuacion >= 0.7:
        return "Bien"
    elif puntuacion >= 0.6:
        return "Suficiente"
    else:
        return "Insuficiente"


puntuacion = raw_input( "Introduce la puntuación: ")

try:
    puntuacion = float( puntuacion)
except:
    print "Tienes que introducir un número"
    quit()

print calcula_calificacion( puntuacion)
