import sys

# Creates the Main Menu
def mainMenu():
    while True:
        print()
        print('''### APU ONLINE SHOPING MALL (AOSM) List ###

        WELCOME WE SELL EVERYTHING HERE RM6.00!!!!

        Select a number for the action that you would like to do:
        
        0. ***View All Categories***
        1. View cart list
        2. Add item to cart list
        3. Remove item from cart list
        4. Check if item is on cart list
        5. How many items on cart list
        6. Clear cart list

        
        7. ###Logout Program###
        ''')

        selection = input("Please select your action: ") # Ask user to select an action

        # User select an action

        if selection =="0":
            DisplayCategory()
        elif selection == "1":
            DisplayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listlength()
        elif selection == "6":
            clearList()
        elif selection == "7":
            sys.exit()
        else:
            print("Invalid Action Innitialized.")

shopping_list = [] # Please add a few items to shopping list

#Sub Menu from main menu

def DisplayCategory():
    while True:
        print()
        print( '''All Catgories: "

        Select number for the action that you would like to do

        11. Item category
        12. Item category-wise
        13. Customer Order
        14. Customer Payment
        
        1.  Exit to Main menu


        7. ###Logout Program###
        ''')
        break
    
    selection = input("Please select your action: ")

    if selection == "11":
        DisplayItemCategory()
    elif selection =="12":
        DisplayWise()
    elif selection =="13":
        pass
    elif selection =="14":
        DisplayPayment()
    elif selection =="1":
        pass
    elif selection == "7":
            sys.exit()


        


#Main Menu Codes
        

# Display all items currently in cart list
def DisplayList():
    print()
    print("------CartList -----")
    for i in shopping_list:
        print ("* " + i)

# Adds an item to cart list
def addItem():
    item = input("Enter the item you wish to have in your shopping list: ")
    shopping_list.append(item)
    print(item + " has been successfully added to the shopping list.")

# Removes an item from cart list
def removeItem():
    item = input("Enter the item you wish to remove in your shopping list: ")
    shopping_list.remove(item)
    print(item + " has been successfully removed from the shopping list.")

# Check to see if a specific item is in cart list
def checkItem():
    item = input("Please select item to check: ")
    if item in shopping_list:
        print("Yes, " + item + " is on shopping list.")
    else:
        print("No, " + item + " is not on shopping list.")

# Items currently in cart list
def listlength():
    print("Items currently >>>", len(shopping_list), "<<<.")

# Delete everything in cart list   
def clearList():
    shopping_list.clear()
    print("Shopping list successfully cleared.")


##### ITEM CATEGORY #####
def DisplayItemCategory():
    while True:
        print()
        print('''Items: "

        Select a number for the category of item category you would like

        15. Cleaning Supplies
        16. Household Items
        17. Stationery
        
        1.  Exit to MAIN MENU

        
        7.  ###Logout Program###
        ''')

        break
    
    selection = input("Please select your action: ")

    if selection == "15":
        DisplayCleaning()
    elif selection =="16":
        DisplayHouse()
    elif selection =="17":
        DisplayStationery()
    elif selection =="1":
        pass
    elif selection == "7":
            sys.exit()

    
### CLEANING SUPPLIES ## **Item Category** 

def DisplayCleaning():
    while True:
        print()
        print('''CLEANING SUPPLIES: "

        Select number for the items you wish to add in cart

        100. Wet Tissues (30 Pcs) 
        101. Melanine Sponges (30 Pcs)
        102. Laundry Basket
        103. Dish Soap
        
        1. Exit to Main menu


        7. ###Logout Program###
        ''')
        
        break
    
    selection = input("Please select your action: ")
    
    if selection == "100":
        tissue()
    elif selection =="101":
        sponge()
    elif selection =="102":
        basket()
    elif selection =="103":
        dishsoap()
    elif selection =="1":
        pass
    elif selection == "7":
            sys.exit()

# Adds CLEANING SUPPLIES to cart #
#As well as confirmation to your selection#

def tissue():
    item = input("ARE YOU SURE you want Wet Tissues? If YES pls type #Wet Tissue to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")

def sponge():
    item = input("ARE YOU SURE you want Melanine Sponges? If YES pls type #Melanine Sponges to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")

    
def basket():
    item = input("ARE YOU SURE you want Laundry Basket? If YES pls type #Laundry Basket to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")

    
def dishsoap():
    item = input("ARE YOU SURE you want Dish Soap? If YES pls type #Dish Soap to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")


### HOUSEHOLD ITEMS ## **Item Category**

def DisplayHouse():
    while True:
        print()
        print('''HOUSEHOLD ITEMS: "

        Select number for the items you wish to add in cart

        110. Lint Roller
        111. Food Container
        112. Toothbrush
        
        1. Exit to Main menu


        7. ###Logout Program###
        ''')
        
        break
    
    selection = input("Please select your action: ")
    
    if selection == "110":
        lint()
    elif selection =="111":
        foodcontainer()
    elif selection =="112":
        toothbrush()
    elif selection =="1":
        pass
    elif selection == "7":
            sys.exit()
            
# Adds HOUSEHOLD ITEMS to cart #
#As well as confirmation to your selection#

def lint():
    item = input("ARE YOU SURE you want Lint Roller? If YES pls type #Lint Roller to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")

def foodcontainer():
    item = input("ARE YOU SURE you want Food Container? If YES pls type #Food Container to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")

    
def toothbrush():
    item = input("ARE YOU SURE you want Toothbrush? If YES pls type #Toothbrush to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")


### Stationery ## **Item Category**
def DisplayStationery():
    while True:
        print()
        print('''STATIONERY: "

        Select number for the items you wish to add in cart

        120. ColourPen (30pcs) 
        121. Scissors
        122. Hihglighter
    
        1. Exit to Main menu


        7. ###Logout Program###
        ''')
        
        break
    
    selection = input("Please select your action: ")
    
    if selection == "120":
        ColourPen()
    elif selection =="121":
        Scissors()
    elif selection =="122":
        Highlighter()
    elif selection =="1":
        pass
    elif selection == "7":
            sys.exit()

# Adds Stationery to cart #
#As well as confirmation to your selection#

def ColourPen():
    item = input("ARE YOU SURE you want ColourPen? If YES pls type #ColourPen to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")


def Scissors():
    item = input("ARE YOU SURE you want Scissors? If YES pls type #Scissors to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")

    
def Highlighter():
    item = input("ARE YOU SURE you want Hihglighter? If YES pls type #Hihglighter to confirm selection: ")
    shopping_list.append(item)
    print(item + " has been succesfully added to the cart. ")


#Item Category-Wise#


def DisplayWise():
    pass


#Customer Payment
#Calculate prices
def DisplayPayment():

    
    Item1=float(input("Item 1="))
    Item2=float(input("Item 2="))
    Item3=float(input("Item 3="))
    
    t=Item1+Item2+Item3
    print("Your Total=",t)
   
    

    


       

# run the function main menu - which will run our application
mainMenu()



