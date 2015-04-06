
import os 
print """-----------------------------REGISTER MACHINE--------------------------------"""
print """ What do you want to do?"""

prices = {}
inventary = {}
total_lista = []
#Opcion inventario
def limpiar():
	del total_lista[:]
	print "Puede ingresar nueva factura."
		
def AddArticle():
	while True:
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
			break
		except ValueError:
			print "insert a valid option"
#Aca ingresara al dic. precios el producto y precio  
	prices[product] = price
	inventary[product]= quantity #producto y cantidad


MENU = True
while MENU == True:
	OPTION = raw_input(" 1. ADD AN ARTICLE \n 2. SELL ARTICLES \n 3. EXIT  ") 
	if OPTION == "3":
		MENU = False
		print "Thank you for using the Register Machine"
	elif OPTION == "2":
		MENU = True
	elif OPTION == "1":
		AddArticle()
		MENU = True
	else: 
		print "please insert a valid option"
