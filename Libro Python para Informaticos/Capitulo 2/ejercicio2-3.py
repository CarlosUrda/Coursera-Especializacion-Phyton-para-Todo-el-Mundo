horas = raw_input( "Introduzca las horas: ")
horas = float( horas)

tarifa = raw_input( "Introduzca la tarifa por hora: ")
tarifa = float( tarifa)

print "Salario: " + str( round( tarifa*horas, 2))
