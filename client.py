import os
from socket import socket, AF_INET, SOCK_DGRAM


host = "192.168.1.162"  # set to IP address of target computer
port = 13002
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input("Enter message to send or type 'exit': ")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
