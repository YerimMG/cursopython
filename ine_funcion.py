#/usr/bin/python 

def INE(x):
	if edad >=18:
		x= "\033[32;1mentregar INE\033[0m "
	else:
		x= "\033[32;1mNo entrgar INE\033[0m "
	return str (x)

while True:
	edad =input("ingresa tu edad : " )
	if edad > 0:
		break 
	else:
		print ("\033[32merror datos inv\033[m")

print " "
print INE(edad)
print " " 