# created by Nicholas Garrett 11/19/2021
# determine the operating system of the system

import sys
import logging
import platform
import os

# info
# return the info of the system
def info(printBool):
    # find the operating system

    system = platform.uname()


    logging.logEntry(f"System: {system.system}")
    logging.logEntry(f"Node Name: {system.node}")
    logging.logEntry(f"Release: {system.release}")
    logging.logEntry(f"Version: {system.version}")
    logging.logEntry(f"Machine: {system.machine}")
    logging.logEntry(f"Processor: {system.processor}\n")

    if(printBool):
        print(f"System: {system.system}")
        print(f"Node Name: {system.node}")
        print(f"Release: {system.release}")
        print(f"Version: {system.version}")
        print(f"Machine: {system.machine}")
        print(f"Processor: {system.processor}")
    return system


# processorFloat
# run a C file to determine based on floating point calculation what your processor is
def processorFloat():
    try:
        os.system("./processorCalculationDetermination")
    except:
        loggin.newError("running ./processorCalculationDetermination failed.  Does the bin. file exist?")
        print("Error found in running that function")

# infoMenu
# small menu to allow the user to run either the info script of the C floating point calculation processor script
def infoMenu():
    loop = True
    while loop:

        choiceToRun = input("Please choose which system information script to run: \n"
                            "\t1: System Information\n"
                            "\t2: Floating Point Calculation processor determination\n"
                            "\tmenu: return to Main Menu \n")

        if choiceToRun == str(1):
            info(True)

        elif choiceToRun == str(2):
            processorFloat()

        elif choiceToRun == "menu":
            print("Returning to Main Menu\n\n\n")
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            loop = False




# function call for testing
# systemInfo()