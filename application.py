import time 
import os
print """-----------------------------REGISTER MACHINE--------------------------------"""
print """ Whant do you want to do?"""

price = {} 
article = {}
Original_list = []

def AddArticle():
	while True:
		insert = raw_input("Insert new article")
		if insert.isalpha():
			insert.lower()
			break
		else:
			print "please insert a valid article"
	while True:
		try:
			quantity = int(raw_input("insert quantity"))
			price = float(raw_input("insert Value"))
			break
		except ValueError:
			print "please insert only numbers"
	article[insert] = quantity
	price[insert] = price


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
	
	
