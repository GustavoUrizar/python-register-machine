import time 
import os
print """-----------------------------REGISTER MACHINE--------------------------------"""
print """ Whant do you want to do?"""



MENU = True
while MENU == True:
	OPTION = raw_input(" 1. ADD AN ARTICLE \n 2. SELL ARTICLES \n 3. EXIT  ") 
	if OPTION == "3":
		MENU = False
		print "Thank you for using the Register Machine"
	elif OPTION == "2":
		MENU = True
	elif OPTION == "1":
		MENU = True
	else: 
		print "please insert a valid option"
	
	
