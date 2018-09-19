# Zhixi Su
# ITP 115 2018Fall
# Assignment 2
# zhixisu@usc.edu

# Assignment 1: Harry Potter Vending Machine
# Define global variable
insDiscount = False
itemName = ""
itenPrice = 0
galleonNum = 0
sickleNum = 0
knutNum = 0

# Customize input coins
isCustomizedInput = input("Would you like input customized number of coin? (Y/N) ")
if isCustomizedInput.upper() == "Y":
    galleonNum = int(input("Input the number of galleon: "))
    sickleNum = int(input("Input the number of sickle: "))
    knutNum = int(input("Input the number of knut: "))
elif isCustomizedInput.upper() == "N":    # Default setting: 1 galleon
    print("Insert 1 galleon to start the machine.")
    galleonNum = 1
else:  # If the user enters an invalid value, then an error message will print and the default setting will apply
    print("You've entered an invalid option. Insert 1 galleon to start the machine.")
    galleonNum = 1

# Vending main menu
print("\nPlease select an item from the vending machine:")
print("\ta) Butterbeer: 58 knuts")
print("\tb) Quill: 10 knuts")
print("\tc) The Daily Prophet: 7 knuts")
print("\td) Book of Spells: 400 knuts")
itemSelected = input()  # Select item
if itemSelected.upper() != "A" or itemSelected.upper() != "B" or itemSelected.upper() != "C" or itemSelected.upper() != "D":
    # Auto-select Butterbeer if inputting an invalid value
    print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
    itemSelected = "a"
shared = input("Will you share this on Instagram? (Y/N) ")
if shared.upper() == "Y":  # To capitalize y/n
    print("Thanks! You get 5 knuts off your purchase")
    insDiscount = True
elif shared.upper() != "N":  # To get rid of violation of invalid input
    print("You have entered an invalid option. No coupon will be used")

# Deal with selected item's information: map the letter to the item it represents and list the price
if itemSelected.upper() == "A":
    itemName = "Butterbeer"
    itemPrice = 58  # Unit: knuts. The same as following
elif itemSelected.upper() == "B":
    itemName = "Quill"
    itemPrice = 10
elif itemSelected.upper() == "C":
    itemName = "The Daily Prophet"
    itemPrice = 7
elif itemSelected.upper() == "D":
    itemName = "Book of Spells"
    itemPrice = 400
if insDiscount:
    coupon = 5
else:
    coupon = 0
# This section above is to make the following section easier to write

# Purchasing page
print("\nYou bought a " + itemName + " for " + str(itemPrice) + " (with coupon of " + str(coupon) + " knuts)", end=" ")
print("and paid with " + str(galleonNum) + " galleon " + str(sickleNum) + " sickle " + str(knutNum) + " knut.")

# Calculating changes
totalInput = 493 * galleonNum + 29 * sickleNum + knutNum
totalChange = totalInput - itemPrice + coupon   # If there is coupon, here we use it. Else, no coupon will be used.
restChange = totalChange  # Define a new variable restChange and use it in following calculation:
galleonChanged = restChange // 493  # Calculating how many galleons can be taken from the change
restChange = restChange % 493  # Here restChange represents the rest of change after taking galleons
sickleChanged = restChange // 29   # Calculating how many sickles can be taken from the rest of changes
restChange = restChange % 29   # Here restChange represents the rest of change after taking galleons and sickles
knutChanged = restChange           # In fact, here the rest of change is the number of knuts

# Change page
print("Here is your change (" + str(totalChange) + " knuts):")
print("Galleons:", str(galleonChanged))
print("Sickles:", str(sickleChanged))
print("Knuts:", str(knutChanged))




# Assignment 2: Choose your own adventure

# Welcome page
print("Welcome to a choose your own adventure game.")

# Story background
print("You are spending your vacation in a quiet town. It's evening now, and you are walking down a street.", end=" ")
print("At this moment, you notice that there is a dark and small valley to your left.\n")

# First select page
print("Do you:")
print("a) Walk into the valley")
print("b) Continue walking down the street")
print("c) Go back to your tavern")
select1 = input()  # select1 represents the first choice

# Branch of second select page
if select1.upper() == "A":  # Branch A: walk into the valley
    print("You walk into the valley. At the end of the valley, there is a wood door decorated with runic words.\n")
    print("Do you:")
    print("a) Knock the door")
    print("b) Leave")
    select2 = input()   # select2 represents the second choice
    if select2.upper() == "A":  # Option A of Branch A
        print("The door opens. You meet a bunch of wizards and witches holding party here. You're invited,", end=" ")
        print("and drink Butterbeer and other magical alcohol with them. A magical night!")
    elif select2.upper() == "B":  # Option B of Branch A
        print("You turn back and flee out of the valley. When you reach the street, you look behind and find that "
              "there is no more a dark valley there.")
    else:  # Get rid of invalid input
        print("You enter an invalid value. Your story ends now.")
elif select1.upper() == "B":  # Branch B: Walk down the street
    print("You meet an old friend walking toward you while you are walking.")
    print("Do you:")
    print("a) Invite him to drink coffee")
    print("b) Chat with him")
    select2 = input()   # select2 represents the second choice
    if select2.upper() == "A":  # Option A of Branch B
        print("In the coffeehouse, both of you enjoy the coffee there a lot. Before you leave to your tavern,", end=" ")
        print("he gives you a bag of top-level coffee bean.")
    elif select2.upper() == "B":  # Option B of Branch B
        print("You chat with him happily, while a thief picks up your and your friend's wallet. OOPS!")
    else:  # Get rid of invalid input
        print("You enter an invalid value. Your story ends now.")
elif select1.upper() == "C":  # Branch C: Go back to your tavern
    print("You walk back to you tavern, where a casino is holding.")
    print("Do you:")
    print("a) Take part in the casino")
    print("b) Go back to your room")
    select2 = input()   # select2 represents the second choice
    if select2.upper() == "A":  # Option A of Branch C
        print("You are so lucky that you win tons of green papers. Now you can travel all over the world!")
    elif select2.upper() == "B":  # Option B of Branch C
        print("You have a wonderful sleep during the night. The next day you are energetic. Enjoy your vacation!")
    else:  # Get rid of invalid input
        print("You enter an invalid value. Your story ends now.")
