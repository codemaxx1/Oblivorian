# create by Nicholas Garrett
# 11/17/2021

#

import portScan
import findOS
import intro
import sniffer

# main
# run all the actual scripts
def main():
    host = "localhost"

    # intro
    introduction = intro.introText()
    print(introduction)

    # determine OS
    operatingSystem = findOS.os();
    if operatingSystem != "linux":
        print("*"*10 + "Be advsed" + "***"*10 + "Your system is not running a Linux operating system.  Oblivorian, this program, is designed to run on a Linux system.  "
                                                "While efforts have been made to ensure Oblivorian runs effectively on non-linux systems, effectiveness can not be gauranteed.  "
                                                "This program is designed to run on Linux.")
    #

    while True:

        choiceToRun = input("Please choose which program to run: \n"
                            "1: Port scan\n"
                            "2: Packet sniffer\n"
                            "3: \n"
                            "4: \n"
                            "5: \n"
                            "quit: Exit program \n")
        print("\n\n")

        if choiceToRun == str(1):
            # port scan
            print("Running port scan\n\tPlease do not close this program while scan is in progress (This process may take several minutes)")
            openPorts = portScan.scan(host);
            print("Port scan complete\n\n")

            print("opening port-close interface")
            portScan.closePortsByUser(openPorts, host)
            print("port-close interface closed")

        elif choiceToRun == str(2):
            print("Running sniffer")
            sniffer.sniffingScan(host)
            Print("closing sniffer")
        #elif choiceToRun == 3:

        #elif choiceToRun == 4:

        #elif choiceToRun == 5:

        elif choiceToRun == "quit":
            print("\nClosing\n")
            exit(1)


if __name__ == '__main__':
    main()
