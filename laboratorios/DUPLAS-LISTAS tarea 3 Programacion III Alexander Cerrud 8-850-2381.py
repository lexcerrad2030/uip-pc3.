'''
tarea # 3 de programacion 3 Alexander Cerrud 8-850-2381
 '''
t2 =("arroz","leche","tuna","cereal","jugo")
lista = []
def menu():
	"""
	esquema del menu para las obciones de las compra del super mercado
	"""

	print ("\n<<<<<<<<<< AGREGUE - ELIMINE U VEA SU LISTA DE PRODUCTOS >>>>>>>>>>\n")
	print ("\t1 - OBCION #1  >>> AGREGAR")
	print ("\t2 - OBCION #2  >>> ELIMINAR")
	print ("\t3 - OBCION #3  >>> VER")
	print ("\t9 - salir")


while True:
	# Mostramos el menu
	menu()


	# solicituamos una opción al usuario
	opcionMenu = input("\n<<<VER MENU E INSETE SU OBCION>>> ")

	if opcionMenu=="1":
		print ("*************************************************")
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n*************************************************\n\nELEMENTOS PARA AGREGAR")
		print(t2[0 : 5])

		print("\nTIENES",len(lista),"AGREGADO -----> ",lista)
		print ("\n*************************************************")

		lista.append( input())

		print ("\nMANTIENES",len(lista),"EN TU LISTA\n")
		print(lista,"<<< New")
		print ("*************************************************")
		input ("")



	elif opcionMenu=="2":
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n*************************************************\n\nPOSEES",len(lista)," ELEMENTOS PARA ELIMINAR\n")
		print(lista)
		print ("\n*************************************************")

		ubicacion = lista.index(input())
		del lista[ubicacion]

		print("TE QUEDAN",len(lista)," ELEMENTO DE TU LISTA" ,lista)
		print ("*************************************************")


		input ("")


	elif opcionMenu=="3":
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n*************************************************\n\nELEMENTOS ACTUALES DE TU LISTA DE PRODUCTOS",len(lista),("\n"))

		print(lista)
		print ("\n*************************************************")

		input("")

	elif opcionMenu=="9":

		print ("*************************************************")
		print ("\nGRACIAS POR SU COMPRA")
		print ("\nTENIAS EN TU LISTA",len(lista), "ELEMENTOS")
		print(lista)
		print ("*************************************************")
		break


	else:
		print ("")
		input("\nATENCION!!! solo teclas que te asignen...\npulsa una tecla para continuar")