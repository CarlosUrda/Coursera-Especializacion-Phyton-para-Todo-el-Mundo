
numero = raw_input( "Introduce un numero: ")

try:
    numero = int( numero)
    print "El numero es " + str( numero)
except:
    print "No has introducido un numero"

