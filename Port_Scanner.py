#imports necessary modules
import pyfiglet
import sys
import socket
from datetime import datetime

#Creates a banner that says PORT SCANNER in ascii art
banner = pyfiglet.figlet_format("PORT SCANNER")
#Displays banner
print (banner)

#this gets the host IPv4 address
target = socket.gethostbyname(socket.gethostname())

#Printing an additional banner
print("*" * 50)
#target is host name/ip address
print("Scanning Target: " + target)
#This line shows start time of program
print("Scanning started at: " + str(datetime.now()))
print("*" * 50)
#end banner

#create list for open ports
openPorts = []

#you can adjust the range here
for port in range(130, 145): #1,65535):
    try:
        #actuall scanning portion
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.setdefaulttimeout(1)

        #This part prints the open ports
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
            #this part adds all opened ports to a list to display later
            openPorts.append("Port {}".format(port))

        elif result != 0:
            print("Port {} is closed".format(port)) 

        s.close()
    except:
        print("Failed")

user_input = input("List all open ports? (y/N) \n")
#converts to lowercase
user_input = user_input.lower()

#determine if user wants to see open ports. Defaults to no
if user_input == 'n':
	exit()
elif user_input == 'y':
	print(openPorts)
else:
	exit()