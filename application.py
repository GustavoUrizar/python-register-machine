
import time
import os 

prices = {}
inventary = {}
total_lista = []
#Opcion inventario
def clean():
	os.system("clear")
	del total_lista[:]
	menus()
		
def AddArticle():
	os.system("clear")
	NewItems = True
	while NewItems == True:
		product = raw_input("insert new article: ")
		if product.isalpha():
			product = product.lower()
			break
		else:
			print "invalid option"
	
	while True:
		try:
			price = float(raw_input("insert price: "))
			quantity = int(raw_input("insert quantity: "))
			prices[product] = price # added new product and price to dictionary
			inventary[product] = quantity #added quantity 
			AnotherArticle()	
		except ValueError:
			print "insert a valid option"

def AnotherArticle():
	others = True
	while others == True:
		other = raw_input("Do you want to add another article? yes or no: ")
		if other in ["yes", "y", "YES", "Y"]:
			AddArticle()
		elif other in ["NO", "no", "n", "N"]:
			os.system("clear")
			menus()		
		else:
			print "insert a valid option"

	
#Opcion caja
def Billing ():
	os.system("clear")
	customer = {} #Dic. local	
	while True:
		try: 
			sell = raw_input("insert article: ")
			sell = sell.lower()
			sellQuantity= int(input("insert quantity: "))
			customer[sell] = sellQuantity #Al dic. se le ingresara el producto que coloque y cantidad
			calc = inventary[sell] - customer[sell] #a inventario le resta el nuevo dic. cliente
			inventary[sell] = calc 
			total = prices[sell] * customer[sell] #precio por la cantidad que ingreso
			total_lista.append(total) #ingresa un valor a total_lista
			AnotherBill()
			break
		except KeyError:
			print "this product is not in inventary please select another one"

def AnotherBill():
	others = True
	while others == True:
		other = raw_input("Do you want to add another article? yes or no: ")
		if other in ["yes", "y", "YES", "Y"]:
			Billing()
		elif other in ["NO", "no", "n", "N"]:
			os.system("clear")
			factura()	
		else:
			print "insert a valid option"
#Opcion facturar
def factura():
	print """
choose an option: 
1 Cash
2 Gold Client
3 Silver Client
""" #Menu	
	while True: 	
		try: 
			opcion = input("> ") #Aca ingresa el cliente la opcion 1 2 o 3
			break
		except (ValueError, NameError):
			print "please insert a valid option from 1 to 3" 
	
	while (opcion >= 4): #Si la opcion es mayor o igual a 4 desplegara
		print "invalid option"		
		opcion = input("> ") #Y volvera a solicitar que de una opcion correcta
	total2 = sum(total_lista) #llama el valor de total_lista
	iva = 0.12
	gold = 0.05
	silver = 0.02
	calc_iva = total2 * iva #Calcula el iva
	iva_agregado = calc_iva + total2 #Agrega el iva a la cantidad
	if opcion == 1: # if the customer does not have any card
		print "loading...."
		time.sleep(2)
		print "your account total is %s plus iva %s" % (total2, calc_iva)
		print "THE GRAND TOTAL IS %s" % iva_agregado
		answer = 0
		while (answer == 0):
			a =	raw_input  ("Do you want to exit from billing? yes or no: ")
			b = a.lower()
			if b == "yes":
				clean()
				answer = 1
			elif b == "no":
				break
				answer = 1
			else:
				print "please insert a valid option"
	elif opcion == 2: #Discount if the customer uses the gold card
		print "loading...."
		time.sleep(2)		
		calc_gold = iva_agregado * gold
		desc_gold = iva_agregado - calc_gold
		print "your account total is %s plus iva %s and the discount for using the gold card is %s" % (total2, calc_iva, calc_gold)
		print "THE GRAND TOTAL IS %s " % desc_gold
		answer = True
		while answer == True:
			a =	raw_input  ("Do you want to exit form billing? yes or no: ")
			b = a.lower()
			if b == "yes":
				clean()
				answer = False
			elif b == "no":
				break
				answer = False
			else:
				print "please insert yes or no"
	elif opcion == 3: #Discount if the customer uses the silver card
		print "Loading...."
		time.sleep(2)		
		calc_silver = iva_agregado * silver
		desc_silver = iva_agregado - calc_silver
		print "your account total is %s plus iva %s and the discount for using the silver card is %s" % (total2, calc_iva, calc_silver)
		print "THE GRAND TOTAL IS %s " % desc_silver
		answer = True
		while answer == True:
			a =	raw_input  ("Do you want to exit form billing? yes or no: ")
			b = a.lower()
			if b == "yes":
				clean()
				answer = False
			elif b == "no":
				break
				answer = False
			else:
				print "please insert yes or no"

def menus():
	MENU = True
	while MENU == True:
		OPTION = raw_input(" 1. ADD AN ARTICLE TO INVENTARY \n 2. SELL ARTICLES \n 3. EXIT  ") 
		if OPTION == "3":
			MENU = False
			print "Thank you for using the Register Machine"
			exit()
		elif OPTION == "2":
			Billing()
			MENU = True
		elif OPTION == "1":
			AddArticle()
			MENU = True
		else: 
			print "please insert a valid option"
os.system("clear")
print """-----------------------------REGISTER MACHINE--------------------------------"""
print """ What do you want to do?"""
print menus()