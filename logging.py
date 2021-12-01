# created by Nicholas
# maintain a log

from datetime import datetime

fileName = "log.txt"

def newError(errorText):
    # open the file
    file = open(fileName, 'a')

    # write error text to the file
    file.write("*"*10 + " ERROR " + "*"*10 + "\t" + str(datetime.now()) + "\n\t" + str(errorText) + "\n" + "*"*10 + " ERROR " + "*"*10  + "\n\n")
    print("*"*10 + " ERROR " + "*"*10 + "\t" + str(datetime.now()) +"\n\t" + str(errorText) + "\n" + "*"*10 + " ERROR " + "*"*10 + "\n\n")

    # close the file
    file.close()


def logEntry(logText):
    # open the file
    file = open(fileName, 'a')

    # write error text to the file
    file.write("-" * 10 + " log " + "-" * 10 + "\t" + str( datetime.now()) + "\n\t" + str(logText) + "\n" + "-" * 10 + " log " + "-" * 10 + "\n\n")
    #print("-" * 10 + " log " + "-" * 10 + "\t" + str( datetime.now()) + "\n\t" + str(logText) + "\n" + "-" * 10 + " log " + "-" * 10 + "\n\n")

    # close the file
    file.close()