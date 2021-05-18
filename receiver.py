import os
from socket import socket, AF_INET, SOCK_DGRAM

host = ""
port = 13005
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
while True:
    (cos, addr) = UDPSock.recvfrom(buf)
    message = cos.decode('utf-8')
    print("Received message: " + message)
    if message == "exit":
        break
UDPSock.close()
os._exit(0)
