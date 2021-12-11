# created by Nicholas Garrett


import sys
import logging
import platform
import os
from random import *
from array import *


# randomizedBruteforce
# bruteforce password guessing function that tries to guess a password through random guessing
"""
    input: the correct password, so the system knows when it has found it
    output
"""
def randomizedBruteforce(correctPassword):
    length = len(correctPassword)
    print("length:" + str(length))

    # the range of ascii values that can be checked
    vals = [32, 126]

    # guess for the password
    randomizedGuess = ""

    # iteration variable
    iteration = 0
    while (randomizedGuess != correctPassword):

        iteration += 1

        # empty the password guess
        randomizedGuess = ""

        # generate guess
        for character in range(0, length):

            # use a random number generat
            guessCharacter = chr( randint(vals[0], vals[1]) )

            # add the new randomly generated character to the guess
            randomizedGuess = randomizedGuess + str(guessCharacter)

        # printing guessed passwords
        print("Random Guess: " + str(randomizedGuess) + "\t iteration: " + str(iteration))




# iterativeBruteforceLoop
# the recursive looping sunction in iterativeBruteforce
"""
"""
def iterativeBruteforceLoop(length, index, iterativeGuessArray):
    logging.logEntry("iterative guess array [" + str(-1) + "]: " + str(iterativeGuessArray[-1]) + "\tbefore")

    # the range of ascii values that can be checked
    vals = [32, 126]

    # update the iterative guess
    iterativeGuessArray[-1] += 1

    # do the rollover for each position in the array
    rollover = False
    for j in range(length):
        i = length-j-1
        logging.logEntry("(boolean) rollover: " + str(rollover))
        if rollover == True:
            logging.logEntry("Rolling over this term and the next")
            iterativeGuessArray[i] += 1
            rollover = False
            if iterativeGuessArray[i] > vals[1]:
                iterativeGuessArray[i] = vals[0]

        #iterativeGuessArray[i] += 1
        logging.logEntry("iterative guess array [" + str(i) + "]: " + str(iterativeGuessArray[i]) + "\tafter")

        if iterativeGuessArray[i] == vals[1]:
            iterativeGuessArray[i] = vals[0]
            rollover = True

        else:
            rollover = False
            break


    # printing guessed passwords
    logging.logEntry("iterated guess: " + str(iterativeGuessArray) )

    return iterativeGuessArray



# iterativeBruteforce
# bruteforce password guessing function that tries to guess a password through guessing through iteratively addressed charcters
"""
    input: the correct password, so the system knows when it has found it
    output
"""
def iterativeBruteforce(correctPassword):
    length = len(correctPassword)
    logging.logEntry("length:" + str(length))

    # the range of ascii values that can be checked
    vals = [32, 126]

    # guess for the password
    iterativeGuess = ""

    # iteration variable
    iteration = 0

    # build the iterative guess string
    iterativeGuessArray = []
    while len(iterativeGuessArray) < length:
        iterativeGuessArray.append(vals[0])
    logging.logEntry("array of initial iterative guesses: " + str(iterativeGuessArray))

    while (iterativeGuess != correctPassword):
        iteration += 1



        iterativeGuessArray = iterativeBruteforceLoop(length, 0, iterativeGuessArray)


        iterativeGuess = ""
        for i in range(0, length):
            iterativeGuess = iterativeGuess + str( chr( iterativeGuessArray[i]) )

        logging.logEntry("guess: \"" + str(iterativeGuess) + "\"")
        print("guess: \"" + str(iterativeGuess) + "\"")

    print("\"" + str(iterativeGuess) + "\" found after after " + str(iteration) + " iterations" )



def menu():
    loop = True
    while(loop):
        choiceToRun = input("Please choose which brute force program to run: \n"
                            "\t1: Randomization\n"
                            "\t2: Iteration\n"
                            "\tmenu: Exit to Main Menu \n")
        print("\n\n")


        if choiceToRun == str(1):
            # port scan
            randomizedBruteforce( input("Please type the correct \"password\"\tex. \"cat\" \nThe longer the password you enter, the longer it will take to find it.  A 4-character password took 2 minutes to crack in testing.\n") )

        elif choiceToRun == str(2):
            iterativeBruteforce( input("Please type the correct \"password\"\tex. \"cat\" \nThe longer the password you enter, the longer it will take to find it.  A 4-character password took 2 minutes to crack in testing.\n") )

        elif choiceToRun == "menu":
            print("Returning to Main")
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            loop = False

# function to call for testing
#iterativeBruteforce("1234")