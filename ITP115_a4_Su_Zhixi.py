# Zhixi Su
# ITP 115 2018Fall
# Assignment 4
# zhixisu@usc.edu

# Import
import random

# Setting up
wordList = ["ape", "create", "ebb", "python", "chimera", "frostbite"]
selectedWord = random.choice(wordList)
jumbleWordList = []

# Jumble the word
selectedWord = list(selectedWord)
selectedCopy = selectedWord[:]
while len(selectedCopy) > 0:
    randomIndex = random.randint(0, len(selectedCopy)-1)
    letter = selectedCopy[randomIndex]
    jumbleWordList.append(letter)
    del selectedCopy[randomIndex]

jumbleWord = "".join(jumbleWordList)

# Testing
print(selectedWord)
print(selectedCopy)
print(jumbleWord)
