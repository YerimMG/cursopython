#/usr/bin/python 


def tab(num,x, y ): 
	for tabla in range (x, y):
		print str(num) + " x " + str(tabla) + " = " + str(num*tabla)
	return str()


print "este prograte multiplicara por rangos"
print " "

#primer termino de la tabla
while True:
	b= input( "del ")
	if b>0:
		break
	else:
		print "nel papu "

#ultimo termino de la tabla
while True:
	x= input( "al ") + 1
	if x>0:
		break
	else:
		print "nel papu "

#este termino, se multiplicara por todos los numeros en la tabla
while True:
	a= input("por ")
	if a>0:
		break
	else:
		print "nel papu"
print " "
print tab(a, b, x )
print "  "