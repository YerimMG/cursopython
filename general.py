#/usr/bin/python 
import math
print "Este programa resuelve la formula general, pero el primer debe ser negativo"
print " "
def formula_general(a, b, c):
#	print "Este programa resuelve la formula general, pero el primer debe ser negativo"
	positivo= (-b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
	negativo= (-b-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
	print " "
	print positivo
	print negativo 
	print " "


a =float(input("Primer digito, negativo: ")) 
b = float(input("segundo digito: "))
c = float(input("ultimo digito: "))

formula_general(a, b, c)