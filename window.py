import tkinter as tk
from tkinter import END
import os
from socket import socket, AF_INET, SOCK_DGRAM
import time

frame = tk.Tk()
frame.title("Worker messenger")
frame.geometry('750x350')
frame.config(background="violet")


def sendMessage(data):
    host = "192.168.8.114"  # będą docelowo def SendMessageDUR i defSendMessageMES z dwoma różnymi IP, ale baza danych wspólna
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


def printInputMes():
    inpmes = inputtxt.get(1.0, "end-1c")
    if inpmes != "":
        lbl.config(text="Problem zgłoszony z wiadomością:\n" + inpmes)
        sendMessage(inpmes)
    else:
        lbl.config(text="Problem zgłoszony")
        sendMessage("alarm")


def alarm():
    lbl.config(text="Alarm zgłoszony")
    return


def cleaner():
    inputtxt.delete(1.0, END)
    lbl.config(text="")


# TextBox Creation
inputtxt = tk.Text(frame,
                   height=12,
                   width=40,
                   font="20")

inputtxt.pack(side = "left")

# Button Creation

alarmButton = tk.Button(frame,
                        text="Wezwij DUR",
                        font="20",
                        bg="red",
                        cursor="spider",
                        height=3,
                        width=20,
                        command=printInput)
alarmButton.pack(side="top")

mesButton = tk.Button(frame,
                      text="Zgłoś problem z MES",
                      font="20",
                      bg="yellow",
                      cursor="spider",
                      height=3,
                      width=20,
                      command=printInputMes)
mesButton.pack(side="top")

clearButton = tk.Button(frame,
                        text="Wyczyść komunikat",
                        font="20",
                        bg="green",
                        cursor="spider",
                        height=3,
                        width=20,
                        command=cleaner)
clearButton.pack(side="top")

closeButton = tk.Button(frame,
                        text="Zamknij",
                        font="20",
                        fg="white",
                        bg="black",
                        cursor="spider",
                        height=3,
                        width=20,
                        command=frame.destroy)
closeButton.pack(side="top")

if __name__ == "__main__":
    label = tk.Label(frame, text="siemka")
    lbl = tk.Label(frame, text="")
    lbl.pack()
    frame.mainloop()
