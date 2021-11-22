# create by Nicholas Garrett
# 11/17/2021

#

import portScan
import findOS
import intro

# main
# run all the actual scripts
def main():
    # intro
    introduction = intro.introText()
    print(introduction)

    print("Beginning Scan:")

    # determine OS
    operatingSystem = findOS.os();
    #

    # port scan
    print("beginning port scan")
    openPorts = portScan.scan("localhost");
    print("port scan complete")

    print("opening port-close interface")
    portScan.closePortsByUser(openPorts)
    print("port-close interface closed")

    print("reccomendations:")



    print("scan complete")

if __name__ == '__main__':
    main()
