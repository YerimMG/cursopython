#/usr/bin/python 
#-*-encoding: utf-8 -*-

Fname =raw_input("primer nombre: " )
Sname =raw_input("segundo nombre: ")
apellido=raw_input("apellido paterno: ")
apellidom=raw_input("apellido materno: ")
dia=raw_input("dia de nacimiento: ")
mes=raw_input("mes de nacimiento: "	)
year = raw_input("year: ")
lista=['puto','culo', 'pipi','cola','pedo', 'mogJ']

MFname= Fname.upper()

if len(Sname)==0:
	name2= MFname[:1]
elif MFname=="JOSE":
	name2=Sname[:1] 
else: 
	name2= Sname[:1]

if len(dia)==1:
	dia2= "0" + str(dia)
else: 
	dia2=dia

if len(mes)==1:
	mes2= "0" + str(mes)
else: 
	mes2=mes

if len(year)==4:
	year2= year[2:]
else: 
	year2=year

x=apellido[:2]
y=apellidom[:1]
z=name2
anio=year2
RFCx= x + y + z
#point= lista.index(RFCx)
print RFCx in lista 
check= RFCx in lista

#if RFCx
#RFC= RFCx + dia2 + mes2 + anio + "xxx"

 
#print RFC.upper()