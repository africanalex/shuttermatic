#!/usr/bin/python

from Tkinter import *
import tkFont
import time, os, subprocess

win = Tk()

myFont = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")

def buttonClicked():
    print("button was clicked")
    exitButton.pack_forget()
    startButton.pack_forget()
    start1Button.pack_forget()
    takePhoto(4)

def button1Clicked():
    print("button was clicked")
    exitButton.pack_forget()
    startButton.pack_forget()
    start1Button.pack_forget()
    take1Photo(1)

def takePhoto(snap):
    if snap > 0:
        countdown(3)
        win.after(10000, takePhoto, snap-1)
    else:
        label["text"] = "Please wait..."
        win.after(100, assAndPrint)

def take1Photo(snap):
    if snap > 0:
        countdown(3)
        win.after(10000, take1Photo, snap-1)
    else:
        label["text"] = "Please wait..."
        win.after(100, assAndPrint1)        
        
def countdown(count):
    label["text"] = count
    if count > 0:
        win.after(1000, countdown, count-1)
    else:
        label["text"] = ""
        win.after(100, callCamera)

def callCamera():
    subprocess.check_output("/home/pi/shuttermatic/boothcamera.sh", shell=True)

def assAndPrint():
    subprocess.call("/home/pi/shuttermatic/assemble_and_print", shell=True)
    label["text"] = "Thanks!"
    startButton.pack(side = LEFT,padx=20)
    start1Button.pack(side = RIGHT, padx=20)
    exitButton.pack(side = BOTTOM)
    
def assAndPrint1():
    subprocess.call("/home/pi/shuttermatic/assemble_and_print_one", shell=True)
    label["text"] = "Thanks!"
    startButton.pack(side = LEFT,padx=20)
    start1Button.pack(side = RIGHT, padx=20)
    exitButton.pack(side = BOTTOM)

def exitProgram():
    win.destroy()




win.title("Photobooth")
win.attributes("-fullscreen", True)
label = Label(win, font = myFont)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label["bg"] = "yellow"
win["bg"] = "yellow"
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram)
exitButton.pack(side = BOTTOM)
img4 = PhotoImage(file="4button.gif")
startButton = Button(win, image = img4, font = myFont, command = buttonClicked)
img1 = PhotoImage(file="1button.gif")
start1Button = Button(win, image=img1, command = button1Clicked)

startButton.pack(side = LEFT,padx=20)
start1Button.pack(side = RIGHT, padx=20)

mainloop()

      
