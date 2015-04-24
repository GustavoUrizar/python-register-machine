"""REGISTER MACHINE"""
import os
import time
SHOPPING = {}
INVENTARY = {} #save the products in inventary
CLIENT = [] #List to save CLIENT's products
PRICES = [] #List to keep the PRICES
TOTAL = [] #save the answer for payment method

"""FUNCTIONS"""
def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def deletedata():
    """Function that clears the lists for a new sale"""
    del CLIENT[:]
    del PRICES[:]
    del TOTAL[:]
    menus()

def addarticle():
    """add articles to the INVENTARY"""
    os.system("clear")
    newitems = True
    while newitems == True:
        product = raw_input("insert new article: ")
        if product.isalpha():
            product = product.lower()
            break
        else:
            print "invalid option"
    while True:
        try:
            price = float(raw_input("insert price: "))
            SHOPPING[product] = price
            INVENTARY[product] = price #added quantity
            print "You have added the following:"
            print INVENTARY
            anotherarticle()
        except ValueError:
            print "insert a valid option"

def anotherarticle():
    """ask if the user wants to add another article to INVENTARY"""
    others = True
    while others == True:
        other = raw_input("Do you want to add another article? yes or no: ")
        other = other.lower()
        if other == "yes":
            addarticle()
        elif other == "no":
            os.system("clear")
            menus()
        else:
            print "Insert only yes or no"

def total():
    """Function that adds the tax to the total"""
    return money() + tax()

def tax():
    """Function that creates the tax"""
    return money() * 0.12

def money():
    """Function that rests the discount from the total"""
    return sum(PRICES) - cards()

def cards():
    """Function that adds the discount to the bill"""
    des = 0
    if "gold" in TOTAL: #if gold is in the list
        des = sum(PRICES) * 0.05 #add to the variable the discount
        return des #it returns the discount when called
    elif "silver" in TOTAL:
        des = sum(PRICES) * 0.02
        return des
    else: #if there is no card, will send 0 discount
        return des

def bill(): #below the %.2f converts in two digits float
    """Function to print the Bill's PRICES"""
    print "Your subtotal is: %.2f" %(sum(PRICES))#this function sums the list
    print "Your discount is: %.2f" %(cards()) #calls the function with 2 decimals
    print "Your Tax is: %.2f" %(tax()) #calls the tax with 2 decimals
    print "Your total is: %.2f" %(total()) #Calls the total with 2 decimals
    print "Thank you for shopping Come back soon"
    enter = raw_input("Press enter to continue")
    deletedata()

def bill_printing():#it prints the bill in order with prices
    """Function to sort the items and print them like a bill"""
    CLIENT.sort()
    temp = [] #temporary list
    for number in CLIENT: #for every item in the dictionary
        PRICES.append(INVENTARY[number]) #it adds the value to another list
        if number not in temp: #if the item is not in temp
            temp.append(number) #lets add it to depurate
    for number in temp: #for everything in the temporary, count the items
        print "Products: " + number
        print "quantity: " + str(CLIENT.count(number))
        print "Unit Price: " + str("%.2f" %(INVENTARY[number]))
        print "-----------------------------------------------------------------"
    bill()

def bill_calc():#it will allow the cashier enter the items to sell
    """Function that asks the cashier for the item"""
    os.system("clear")
    calculus = True
    while calculus == True:
        try:
            cashier = raw_input("Enter the item: ")
            cashier = cashier.lower()
            if cashier == "done": #sends the program to another function
                clear()
                bill_printing()
                calculus = False #kills the function
            elif cashier == "gold":
                TOTAL.append("gold") #it sends gold to an empty list
            elif cashier == "silver":
                TOTAL.append("silver")
            elif cashier == "silver" and "gold":
                TOTAL.append("gold")
            elif cashier not in INVENTARY: #it verifies than the item is in the store
                print "Item not in store"
                mainmenu()
            else:
                CLIENT.append(cashier)#adds the item to the new list
        except ValueError:
            print "Enter only items"

def mainmenu():
    """if the item is not in stock ask to go back to menu"""
    others = True
    while others == True:
        other = raw_input("Do you want to go back to the main menu? yes or no: ")
        other = other.lower()
        if other == "yes":
            os.system("clear")
            menus()
        elif other == "no":
            os.system("clear")
            bill_calc()
        else:
            print "insert a valid option"

def menus():
    """provide the menu"""
    os.system("clear")
    print """-----------------------------REGISTER MACHINE--------------------------------"""
    print """ What do you want to do?"""
    menu = True
    while menu == True:
        option = raw_input(" 1. ADD AN ARTICLE TO INVENTARY \n 2. SELL ARTICLES \n 3. EXIT  ")
        if option == "3":
            menu = False
            print "Thank you for using the Register Machine"
            exit()
        elif option == "2":
            bill_calc()
            menu = True
        elif option == "1":
            addarticle()
            menu = True
        else:
            print "please insert a valid option"
            time.sleep(2)
            os.system("reset")

os.system("clear")
print """-----------------------------REGISTER MACHINE--------------------------------"""
print """ What do you want to do?"""
print menus()
