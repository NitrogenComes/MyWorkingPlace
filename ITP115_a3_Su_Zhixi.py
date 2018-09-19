# Zhixi Su
# ITP 115 2018Fall
# Assignment 3
# zhixisu@usc.edu

# Import
import random

# Part 1: Igpén Lvísheá (Pig Elvish)

# Input page
print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!\n(Welcome to the Pig Elvish translator!)")
anotherWord = True
while anotherWord:
    englishWord = input("Please enter the word you want to translate: ")

# Translating
    # 1. Take the first letter to the end
    newWord = englishWord[1:] + englishWord[0]  # Keep "word" string itself for further use
    # 2. & 3. Add letters to the end of "newWord"
    if len(newWord) >= 4:
        newWord = newWord + random.choice("aeiou")
    elif len(newWord) <= 3:
        newWord = newWord + "en"
    # 4. Change all k's to c's
    newWord.replace("k", "c")
    newWord.replace("K", "C")  # including capital K and lowercase k
    # 5. Change e at the end of newWord to the "e" with two dots above it
    if newWord[-1] == "e":
        newWord = newWord[:-1] + "ë"
    # 6. Handle capitalized letters
    if englishWord[0].isupper():
        newWord = newWord.capitalize()
    # 7. (Bonus) Replace "aeiou" with "áéíóú"
    elvishOutcome = ""
    letterAppend = ""
    for letter in newWord:
        coin = random.randint(0, 2)  # 0 ==> not replace, 1 ==> replace
        if coin == 1:
            if letter == "a":
                letterAppend = "á"
            elif letter == "e":
                letterAppend = "é"
            elif letter == "i":
                letterAppend = "í"
            elif letter == "o":
                letterAppend = "ó"
            elif letter == "u":
                letterAppend = "ú"
            else:
                letterAppend = letter
        else:
            letterAppend = letter
        elvishOutcome = elvishOutcome + letterAppend
        # Each time append a letter to the string elvish Outcome until all letters in newWord are checked

# Print page & Ask for another translation
    print("The word", englishWord, "in Elvish is", elvishOutcome + ".")
    runAgain = input("Would you like to translate another word? Y/N ")
    while runAgain.upper() != "Y" and runAgain.upper() != "N":
        print("Invalid input. Try again.")
        runAgain = input("Would you like to translate another word? Y/N ")
    if runAgain.upper() == "N":
        print("Oodbyega! Aveha aen icenë ayden!\n(Goodbye! Have a nice day!)")
        anotherWord = False


# Part 1 (bonus): Translate Pig Elvish back to English (Imperfectly)
""" To translate Pig Elvish back, following steps are going to execute
    1. Turn all "áëéíóú" to normal "aeiou"
    2. Check the letter at the end of the word. If it is "en", cut the last 2 letters; else, cut the last letter
    3. Put the current last letter to the front of the word
    4. Handle capitalized letters
    Problem: Since we have no clue which c is transferred from k and which c is originally c, this translation is not
    fully reversible. As a result, the outcome may be not exactly the English word as we expected.
    Example: uíccqí (quick) will be translated as quicc."""

anotherElvish = True
while anotherElvish:
    elvishWord = input("Please enter the Elvish word you want to translate back: ")
    # 1. Turn all "áëéíóú" to normal "aeiou"
    median = ""
    letterAppend = ""
    for letter in elvishWord:
        if letter == "á":
            letterAppend = "a"
        elif letter == "ë" or letter == "é":
            letterAppend = "e"
        elif letter == "í":
            letterAppend = "i"
        elif letter == "ó":
            letterAppend = "o"
        elif letter == "ú":
            letterAppend = "u"
        else:
            letterAppend = letter
        median = median + letterAppend
    # 2. Cut the tail of the elvish
    if median[-1] == "n":
        median = median[:-2]
    else:
        median = median[:-1]
    # 3. Put the last letter to the front
    median = median[-1] + median[:-1]
    # 4. Handle capitalized letters
    if elvishWord[0].isupper():
        englishOutput = median.capitalize()
    else:
        englishOutput = median
    # Print page & Ask for another translation
    print("The word", elvishWord, "is", englishOutput, "in English.")
    runAgain = input("Would you like to translate another word? Y/N ")
    while runAgain.upper() != "Y" and runAgain.upper() != "N":
        print("Invalid input. Try again.")
        runAgain = input("Would you like to translate another word? Y/N ")
    if runAgain.upper() == "N":
        print("Oodbyega! Aveha aen icenë ayden!\n(Goodbye! Have a nice day!)")
        anotherElvish = False

# Part 2: Largest Number

# Define variables and lists
continueInput = True
numberList = []
maxNum = 0

# Input numbers
print("Input an integer greater than or equal to 0 or -1 to quit: ")
while continueInput:
    inputNum = int(input())
    numberList.append(inputNum)
    if inputNum < 0:
        continueInput = False

# Find the maximum in the list
for number in numberList:
    if number > maxNum:
        maxNum = number

# Print page
print("The largest number is", str(maxNum) + ".")
