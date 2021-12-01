# created by Nicholas

import os
import socket

import logging

def sniffingScan(host):
    logging.logEntry("running sniffer")

    host = socket.gethostbyname(host)

    # identify the protocol type to listen for
    if os.name == 'nt':
        protocol = socket.IPPROTO_IP
    else:
        protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol)

    sniffer.bind((host, 8080))

    # include IP header
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    #read a packet
    print(sniffer.recvfrom(65565))



sniffingScan("locahost")
