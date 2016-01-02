#coding=utf-8

horas = raw_input( "Introduce las horas: ")
try:
    horas = float( horas)
except:
    print "Tienes que introducir horas en formato numérico"
    quit()

tarifa = raw_input( "Introduce la tarifa: ")
try:
    tarifa = float( tarifa)
except:
    print "Tienes que introducir la tarifa en formato numérico"
    quit()

if horas > 40:
    salario = 40*tarifa + 1.5*tarifa*(horas-40)
else:
    salario = tarifa*horas

print "El salario es: " + str( salario)

