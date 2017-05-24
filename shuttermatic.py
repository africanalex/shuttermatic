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
        win.after(10000, takePhoto, snap-1)
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
    startButton.pack()
    start1Button.pack()
    exitButton.pack(side = BOTTOM)
    
def assAndPrint1():
    subprocess.call("/home/pi/shuttermatic/assemble_and_print_one", shell=True)
    label["text"] = "Thanks!"
    startButton.pack()
    start1Button.pack()
    exitButton.pack(side = BOTTOM)

def exitProgram():
    win.destroy()

win.title("Photobooth")
win.attributes("-fullscreen", True)
label = Label(win, font = myFont)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label["bg"] = "yellow"
win["bg"] = "yellow"
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack(side = BOTTOM)
startButton = Button(win, text = "Start 4", font = myFont, command = buttonClicked, height = 2, width = 8)
startButton.pack()
start1Button = Button(win, text = "Start 1", font = myFont, command = button1Clicked, height = 2, width = 8)
start1Button.pack()

mainloop()

      
