def Menu():
	print ("""
Calculadora

Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")
def Calculadora():
	Menu()
	opc=int(input("Seleccióne opción \n"))
	while(opc>0 and opc<5):
		x = int(input("Ingrese numero \n"))
		y = int(input("Ingrese otro numero \n"))
		if (opc==1):
			print ("El resultado es:",x+y)
			opc=int(input("Seleccióne opción \n"))
		elif(opc==2):
			print ("El resultado es:",x-y)
			opc=int(input("Seleccióne opción \n"))
		elif (opc==3):
			print ("El resultado es:",x*y)
			opc=int(input("Seleccióne opción \n"))
		elif (opc==4):
			try:
				print ("El resultado es:",x/y)
				opc=int(input("Seleccióne opción \n"))
			except ZeroDivisionError:
				print ("No se permite la division entre 0")
				opc=int(input("Seleccióne opción \n"))
Calculadora()
