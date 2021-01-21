#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
ports = []

host = input("[*]Enter the host to scan: ")
"""number_of_ports = int(input("Enter the number of ports to scan: "))
for i in range(0,number_of_ports):
	ports.append(int(input("Enter port: ")))
"""


def portScanner(args):
	#for port in ports: -> Unhash this if you need to specify the ports yourself
	if sock.connect_ex((host, port)):
		print(colored("Port ",port, " is closed", 'red'))
	else:
		print(colored("Port ",port, " is open", 'green'))

#portScanner(ports)

#Scanning the first 1000 ports
for port in range(1,1000):
	portScanner(port)