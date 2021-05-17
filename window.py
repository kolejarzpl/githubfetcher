import tkinter as tk
from tkinter import END
import os
from socket import socket, AF_INET, SOCK_DGRAM
import time

frame = tk.Tk()
frame.title("Worker messenger")
frame.geometry('400x200')


def sendMessage(data):
    host = "192.168.1.162"  # set to IP address of target computer
    port = 13005
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    message = bytes(data, "utf-8")
    UDPSock.sendto(message, addr)
    UDPSock.close()


def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    if inp != "":
        lbl.config(text="Awaria zgłoszona z wiadomością:\n" + inp)
        sendMessage(inp)
    else:
        lbl.config(text="Awaria zgłoszona")
        sendMessage("alarm")

def alarm():
    lbl.config(text="Alarm zgłoszony")
    return


def cleaner():
    inputtxt.delete(1.0, END)
    lbl.config(text="")


# TextBox Creation
inputtxt = tk.Text(frame,
                   height=5,
                   width=20)

inputtxt.pack()

# Button Creation

alarmButton = tk.Button(frame,
                        text="Zgłoś awarię",
                        command=printInput)
alarmButton.pack()

okButton = tk.Button(frame,
                        text="Wyczyść komunikat",
                        command=cleaner)
okButton.pack()



if __name__ == "__main__":
    label = tk.Label(frame, text="siemka")
    lbl = tk.Label(frame, text="")
    lbl.pack()
    frame.mainloop()
