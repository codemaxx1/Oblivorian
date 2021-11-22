# created by Nicholas Garrett 11/19/2021
# determine the operating system of the system

import sys
import logging


# os
# return the name of the operating system
def os():
    # find the operating system
    operatingSystem = sys.platform
    logging.logEntry("Operating System: " + operatingSystem)

    return operatingSystem

