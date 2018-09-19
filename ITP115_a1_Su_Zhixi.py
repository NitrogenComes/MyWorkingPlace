# Zhixi Su
# ITP 115 2018Fall
# Assignment A1
# zhixisu@usc.edu

"""
Assignment: to write a mad lib
5 strings, 3 integers, 1 float number at least
Signify the input word with ("") e.g. "42"
At least 2 numbers must be used in some calculations
"""

# Input 5 strings
place = input("Please name a location: ")
nameA = input("Name your favorite actor: ")
nameB = input("Name your second favorite actor: ")
petType = input("Choose an animal as their pet: ")
petName = input("Name the pet: ")
# Input 3 integers
gasNeeded = int(input("Enter your lucky number here: "))
distance = int(input("Enter a number that is larger than 10 but less than 20: "))
minute = int(input("Enter a number that is less than 10: "))
# Input a number with a decimal
gasPrice = float(input("Estimate the gas price today: "))

"""
# testing inputs:
place = "a"
nameA = "b"
nameB = "c"
petType = "dog"
petName = "d"
gasNeeded = 10
distance = 15
minute = 10
gasPrice = 5.2
"""

# Calculation
totalPrice = gasNeeded * gasPrice

# Transfer all numbers to strings
gasNeeded = str(gasNeeded)
distance = str(distance)
minute = str(minute)
gasPrice = str(gasPrice)
totalPrice = str(totalPrice)

# Output
print("One day \"" + nameA + "\" and \"" + nameB + "\" took their pet \"" + petType + "\" named \"" + petName + "\" to the pet hospital at \"" + place + "\".", end=" ")
print("After driving for \"" + distance + "\" miles, they passed by a gas station and \"" + nameB + "\" wanted to refill the gas tank.", end=" ")
print("The gas station staff said that their gas was \"" + gasPrice + "\" per gallon", end=" ")
print("They needed \"" + gasNeeded + "\" gallons gas, so they needed to pay \"" + totalPrice + "\" dollars.", end=" ")
print("\"" + nameA + "\" thought that the price was too expensive, and soon they left the gas station.", end=" ")
print("However, after \"" + minute + "\" minutes, they ran out of their gas. They had to walk back to the station and accept the expensive price they used to consider.")
