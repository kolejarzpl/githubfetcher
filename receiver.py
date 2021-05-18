import tkinter as tk
from tkinter import END
import os
from socket import socket, AF_INET, SOCK_DGRAM
import time
from time import sleep

frame = tk.Tk()
frame.title("Receiver")
frame.geometry('750x350')
frame.config(background="violet")


# var = tk.StringVar()
# var.set('hello')

# host = ""
# port = 13005
# buf = 1024
# addr = (host, port)
# UDPSock = socket(AF_INET, SOCK_DGRAM)
# UDPSock.bind(addr)
# lbl1 = tk.Label(frame,
#                text="Waiting to receive messages...")
# lbl1.pack()
# while True:
#     (cos, addr) = UDPSock.recvfrom(buf)
#     message = cos.decode('utf-8')
#     lbl2 = tk.Label(frame,
#                     text=message)
#     lbl2.pack()
#     if message == "exit":
#         break
# UDPSock.close()
# os._exit(0)



# if __name__ == "__main__":
#     label = tk.Label(frame, text="siemka")
#     lbl = tk.Label(frame, text="")
#     lbl.pack()
#     frame.mainloop()



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
