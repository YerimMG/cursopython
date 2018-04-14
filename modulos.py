#/usr/bin/python 
#-*-encoding: utf-8 -*-

#calculadora.float
print " "
print "Datos "
print " "
print "calculadora = 1 "
print "tabla de multiplicar = 2"
print "INE = 3"
print "Formula general = 4 "
print "RFC = 5 "
print " "
x = raw_input("Que operacion quiere hacer? " )
print " "

if x == "1" :
	import calculadora_funcion 

elif x == "2":
	import while_funcion

elif x == "3":
	import ine_funcion
elif x == "4":
	import general
elif x== "5":
	import genera_RFC
else:
	print "no te entiendi "