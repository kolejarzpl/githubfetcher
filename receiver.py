import os
import time
import tkinter as tk
from socket import socket, AF_INET, SOCK_DGRAM
from tkinter import END
from tkinter import messagebox

frame = tk.Tk()
frame.title("Host")
frame.withdraw()

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
    messagebox.showinfo("Alarmy","Otrzymana wiadomość: \n"+message)
    print("Otrzymana wiadomość: " + message)
    if message == "exit":
        break

UDPSock.close()
os._exit(0)
