#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.100.72"
port = 443

def portScanner(port):
	if sock.connect_ex((host, port)):
		print("Port ",port, " is closed")
	else:
		print("Port ",port, " is opened")


portScanner(port)