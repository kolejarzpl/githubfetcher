import os
import time
import tkinter as tk
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep
from tkinter import END
from tkinter import messagebox
from threading import *

frame = tk.Tk()
frame.title("Host message")
frame.geometry('300x280')
frame.config(background="violet")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        frame.destroy()

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
    lbl = tk.Label(frame,
                   text="Received message:\n"+message,
                   font="30")
    lbl.pack()
    frame.protocol("WM_DELETE_WINDOW", on_closing)
    frame.mainloop()
    print("Received message: " + message)

    if message == "exit":
        break

print('test)')
UDPSock.close()
os._exit(0)


# if __name__ == "__main__":
#     label = tk.Label(frame, text="siemka")
#     lbl = tk.Label(frame, text="")
#     lbl.pack()
#     frame.mainloop()
