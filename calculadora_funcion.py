#/usr/bin/python 

print "esta calculadora solo sirve con los digitos +, -, *, x, / "
print " "

def calculadora(a, operacion, b):
	print " "
	if operacion == "+":
		x= float(a)+float(b)
	elif operacion == "-":
		x= float(a)-float(b)
	elif operacion == "x" or operacion == "*":
		x= float(a)*float(b)
	elif operacion == "/":
		x= float(a)/float(b)

	return str(x)

#print a=input("operacion de dos numeros: ") + operacion=raw_input() + b=input()
while True:
	a= raw_input( "primer digito ")
	if a.isdigit() and len(a)>0:
		break	
	else: 
		print "error"


while True:
	operacion= raw_input( "operacion ")
	if operacion== "+" or operacion== "-" or operacion== "x" or operacion== "*" or operacion== "/":
		break
	else: 
		print "error"


while True:
	c= raw_input( "segundo digito ")
	if c.isdigit() and len(c)>0:
		break	
	else: 
		print "error"

print "el resultado de " + str(a) + str(operacion) + str(c) + " = " + calculadora(a, operacion ,c ) 
print " "