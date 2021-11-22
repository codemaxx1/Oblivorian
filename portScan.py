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

    for port in range(portMin, portMax):

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

    # return the open ports
    return openPorts




# closePortsByUser
# allow the user to control which ports to close
"""
    input: openPorts, an array of the open ports to allow the user to close
    output:
"""
def closePortsByUser(openPorts):
    logging.logEntry(openPorts)
