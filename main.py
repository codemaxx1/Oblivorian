# create by Nicholas Garrett
# 11/17/2021

#
import os

import portScan
import systemInfo
import intro
import sniffer
import passwordCracker
# main
# run all the actual scripts
def main():
    host = "localhost"

    # intro
    introduction = intro.introText()
    print(introduction)

    # determine OS
    operatingSystem = systemInfo.info(False);
    if operatingSystem.system != "Linux":
        print("*"*10 + " Be advised " + "*"*10 + "\nYour system is not running a Linux operating system.  Oblivorian, this program, is designed to run on a Linux system.  \n"
                                                "While efforts have been made to ensure Oblivorian runs effectively on non-linux systems, effectiveness can not be gauranteed.  \n"
                                                "\n \n")
    #

    while True:

        choiceToRun = input("Please choose which program to run: \n"
                            "\t1: Port scan\n"
                            "\t2: Packet sniffer (incomplete)\n"
                            "\t3: System Information\n"
                            "\t4: Password Cracker\n"
                            "\t: \n"
                            "\tquit: Exit program \n")
        print("\n\n")

        if choiceToRun == str(1):
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            # port scan
            print("Running port scan\n\tPlease do not close this program while scan is in progress (This process may take several minutes)")
            openPorts = portScan.scan(host);
            print("Port scan complete\n\n")

            print("opening port-close interface")
            portScan.closePortsByUser(openPorts, host)
            print("port-close interface closed")

        elif choiceToRun == str(2):
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            print("Running sniffer")
            sniffer.sniffingScan(host)
            print("closing sniffer")

        elif choiceToRun == str(3):
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            systemInfo.infoMenu()

        elif choiceToRun == str(4):
            print("Running Password Cracker")
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            passwordCracker.menu()
            print("closing password cracker")

        elif choiceToRun == str(5):
            print("Running Shadow file reader")
            print("\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n\t.\n")
            shadowFileReader.read()
            print("closing Shadow file reader")

        elif choiceToRun == "quit":
            print("\nClosing\n")
            exit(1)


if __name__ == '__main__':
    main()
