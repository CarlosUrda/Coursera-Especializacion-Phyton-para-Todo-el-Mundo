
horas = raw_input( "Elige las horas: ")
try:
    horas = float( horas)
except:
    print "Introduce las horas correctamente"
    quit()

razon = raw_input( "Elige la razon por hora: ")
try:
    razon = float( razon)
except:
    print "Introduce la razon correctamente"
    quit()

if horas > 40: 
    resultado = 40 * razon + (horas-40)*1.5*razon
else:
    resultado = horas * razon

print "Resultado: ", resultado

