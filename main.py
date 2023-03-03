import random

def pickWord(filename): 
    file = open(filename, "r")
    words = [word.strip() for  word in list(file.readlines())]
    return random.choice(words)

def updateGuess(wordToGuess, currentGuess, newChar):
    temp = currentGuess
    for x in range(len(wordToGuess)):
        if wordToGuess[x] == newChar:
            temp = temp[:x] + newChar + temp[x+1:]
    return temp


wordToGuess = pickWord("keywords.txt")

print(wordToGuess)

display = "_" * len(wordToGuess)
guesses = 52


print(display)

gameWon = False


while not gameWon:
    usrInput = input("Guess a letter:  ")
    if usrInput in wordToGuess:
        display = updateGuess(wordToGuess, display, usrInput)
    print(display)
    if display == wordToGuess:
        gameWon = True

print("You win!")
