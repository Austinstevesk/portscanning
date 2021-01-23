#!/usr/bin/python


#Running the program
#1. python advanced_scanner.py -H AS -p 135,110,80,50,3306 -> Name is resolved
#2. python advanced_scanner.py -H 192.168.10.10 -p 135,110,80,50,3306
#3. python advanced_scanner.py -H google.com -p 135,110,80,50,3306


from socket import *
import optparse
from threading import *


def connScan(tgtHost, tgtPort): #Returns whether the port is closed or open
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print("[+] tcp Open ", tgtPort)
	except:
		print("[-] tcp Closed ", tgtPort)

	finally:
		sock.close()


def portScan(tgtHost, tgtPorts): #Resolves names and addresses
	try:
		tgtIP = gethostbyname(tgtHost) #Resolves name
	except:
		print("Unknown target host", tgtHost) #If the name isn't resolved
	try:
		tgtName = gethostbyaddr(tgtIP) 
		print("[+] Scan results for: ", tgtName[0]) 
	except:
		print("[+] Scan results for: ", tgtIP)

		setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=[tgtHost, int(tgtPort)]) #Runs the connScan function
		t.start()

def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>') #Prints program usage
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')

	if (tgtHost == None or (tgtPorts[0]) == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost, tgtPorts) #Runs the portScan function
if __name__ == '__main__': 
	main()