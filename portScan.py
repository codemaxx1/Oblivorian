# created by Nicholas Garrett 11/15/2021
# implementations for port scan

import sys
import socket
from datetime import datetime
import subprocess
import os
import logging


# scan
# scan the ip address specified
"""
    input: host, the ip address to scan
    output: array of open ports
"""
def scan(host):
    openPorts = []
    portMin = 1
    portMax = 65535

    target = socket.gethostbyname(host)

    logging.logEntry(str("Beginning scan of " + str(target) + " at " + str(datetime.now())))

   # print("/ " + "^"*100 + " \ ")
    iteration = 1;
    dist = (portMax - portMin) / 100
    distRange = 0
    #print("distribution:" + str(dist))

    #print("< |", end="\r")

    for port in range(portMin, portMax):
        iteration = iteration + 1

        #print("dist = " + str(dist) + "\t iterations: " + str(iteration))

        # status bar of port scan
        if iteration > distRange:
            #print("distRange = " + str(distRange) + "\t iterations: " + str(iteration))
                    distRange= distRange + dist

        try:

            # connect to socket
            #                       family      type
            s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

            socket.setdefaulttimeout(1)

            # attempt to connect to the port
            result = s.connect_ex((target, port))


            # if we are able to connect
            if result == 0:
                # try to get tcp buffer return from the port
                try:
                    data = s.recv(1240)
                except:
                    string = str("unable to retrieve buffer data from port" + str(port))
                    logging.logEntry(string)


                logging.logEntry(str("Port " + str(port) + " is open"))



                command = "sudo netstat -ltnp | grep " + str(port)

                # get the process information for the port
                try:
                    stdoutdata = subprocess.check_output(command, shell=True)
                    stdoutdata = stdoutdata.decode("utf-8")
                    process = stdoutdata.split("LISTEN")
                    process = process[-1].split()
                    #process = process[-1]
                    logging.logEntry(str("process: " + str(process)))
                except:
                    process = "unknown"
                    logging.logEntry("")


                logging.logEntry(str("data: %s\n" % data) )

                # append port and process information to array
                openPorts.append([port, process])
            s.close()

        except socket.gaierror:
            logging.newError("Hostname unable to be resolved")

        except socket.error:
            logging.newError("Server not responding")

    print(" >")
    # return the open ports
    return openPorts




# closePortsByUser
# allow the user to control which ports to close
"""
    input: openPorts, an array of the open ports to allow the user to close
    output:
"""
def closePortsByUser(openPorts, host):
    logging.logEntry(openPorts)

    ports = []
    # make an array of the ports
    for port in openPorts:
        ports.append(port[0])
    print("Open Ports: " + str(ports) + "\n")


    print("To prevent attack to you system, it is recommended that you terminate the processes llistening to these ports: ")

    # iterate thorugh all the open ports
    for port in openPorts:
        deletePort = input("Do you wish to terminate the process on " + str(host) + " at port " + str(port[0]) + "?  It is run by the program " + str(port[1]) + "\n (YES) or (NO)\n" )
        #print(deletePort)

        # confirm that the user wants to terminate this ports
        if deletePort.upper() == "YES":
            confirmed = input("Are you sure?  Closing this port may cause " + str(port[1]) + " to malfunction or fail.\n(YES) or (NO)\n")
            #print(confirmed)

            # if the user confirms they want to terminate the process listening to the port, kill it
            if confirmed.upper() == "YES":
                killCommand = "kill - 9 $(lsof - t - i:" + str(port[0]) + ")"


                # get the process information for the port
                try:
                    logging.logEntry("killing process")
                    stdoutdata = subprocess.check_output(killCommand, shell=True)
                except:
                    logging.newError("termination error, " + str(host) + " " + str(port[0]) + "was not able to be killed")

                if( stdoutdata ):
                    print( str(host) + " " + str(port[0]) + "has been successfully terminated")

                else:
                    print("Some error occured" + str(host) + " " + str(port[0]) + " was unable to be terminated\n")

            else:
                print("YES command not given.  Canceling program termination\n")

        else:
            print("YES command not given.  Canceling program termination\n")