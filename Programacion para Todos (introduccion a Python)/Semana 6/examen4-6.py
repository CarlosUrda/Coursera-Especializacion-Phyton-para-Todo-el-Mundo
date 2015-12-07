#coding=utf-8

def computepay( horas, tarifa):
    if horas > 40:
        salario = 40*tarifa + 1.5*tarifa*(horas-40)
    else:
        salario = tarifa*horas
    
    return salario


try:
    horas = raw_input( "Introduce las horas: ")
    horas = float( horas)
    tarifa = raw_input( "Introduce la tarifa: ")
    tarifa = float( tarifa)
except:
    print "Tienes que introducir datos numéricos"
    quit()


salario = computepay( horas, tarifa) 
print "El salario es: " + str( salario)

