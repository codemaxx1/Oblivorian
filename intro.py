# created by Nicholas Garrett 11/19/2021
# print a header and starting information about the Oblivorian vulnerability scanner

import pyfiglet
import logging

def introText():

    ascii_banner = pyfiglet.figlet_format("Oblivorian")
    logging.logEntry(ascii_banner)

    return ascii_banner
