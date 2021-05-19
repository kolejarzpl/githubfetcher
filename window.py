import tkinter as tk
from tkinter import END
import os
from socket import socket, AF_INET, SOCK_DGRAM
import time
import tkinter.messagebox

frame = tk.Tk()
frame.title("Worker messenger")
frame.geometry('300x280')
frame.config(background="violet")


def sendMessage(data):
    host = "192.168.0.85"  # będą docelowo def SendMessageDUR i defSendMessageMES z dwoma różnymi IP, ale baza danych wspólna
    port = 13005
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    message = bytes(data, "utf-8")
    UDPSock.sendto(message, addr)
    UDPSock.close()


def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    if inp != "":
        tk.messagebox.showinfo(title="Sukces", message="Awaria zgłoszona z wiadomością:\n" + inp)
        sendMessage(inp)
        inputtxt.delete(1.0, END)
    else:
        tk.messagebox.showinfo(title="Sukces", message="Awaria zgłoszona")
        sendMessage("alarm")
        inputtxt.delete(1.0, END)


def printInputMes():
    inpmes = inputtxt.get(1.0, "end-1c")
    if inpmes != "":
        tk.messagebox.showinfo(title="Sukces", message="Problem zgłoszony z wiadomością:\n" + inpmes)
        sendMessage(inpmes)
        inputtxt.delete(1.0, END)
    else:
        tk.messagebox.showinfo(title="Sukces", message="Problem zgłoszony")
        sendMessage("MES nie działa")
        inputtxt.delete(1.0, END)


# def alarm():
#     lbl.config(text="Alarm zgłoszony")
#     return


def cleaner():
    inputtxt.delete(1.0, END)
    lbl.config(text="")


# TextBox Creation
inputtxt = tk.Text(frame,
                   height=4,
                   width=30,
                   font="20")

inputtxt.pack(side = "top")

# Button Creation

alarmButton = tk.Button(frame,
                        text="Wezwij DUR",
                        font="20",
                        bg="red",
                        cursor="spider",
                        height=3,
                        width=30,
                        command=printInput)
alarmButton.pack(side = "top")

mesButton = tk.Button(frame,
                      text="Zgłoś problem z MES",
                      font="20",
                      bg="yellow",
                      cursor="spider",
                      height=3,
                      width=30,
                      command=printInputMes)
mesButton.pack(side = "top")

clearButton = tk.Button(frame,
                        text="Wyczyść komunikat",
                        font="20",
                        bg="green",
                        cursor="spider",
                        height=1,
                        width=30,
                        command=cleaner)
clearButton.pack(side = "top")

closeButton = tk.Button(frame,
                        text="Zamknij",
                        font="20",
                        fg="white",
                        bg="black",
                        cursor="spider",
                        height=1,
                        width=30,
                        command=frame.destroy)
closeButton.pack(side = "top")

if __name__ == "__main__":
    lbl = tk.Label(frame, text="")
    lbl.pack()
    frame.mainloop()
