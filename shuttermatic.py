#!/usr/bin/python

from Tkinter import *
import tkFont
import time, os, subprocess

win = Tk()

myFont = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")
def photo_count():
    import os
    if(os.path.isfile('./f_count.txt')):
        m = open('f_count.txt', 'r')
        n = int(m.read())
        if n <= 35:
            m.close()
            m = open('f_count.txt', 'w')
            s = str(n + 1)
            m.write(s)
            m.close()
            print('Photo number '+s)
            button1Clicked()
        else:
            print('Please Check Catredge')
            label["text"] = "Please Check Catredge"
            m.close()
            #Create a buttlon here that says Checked or Cancel
            #if cancel it will terminate the process

    else:
        new = open('f_count.txt', 'w')
        new.write('0')
        new.close()
        photo_count()

def checked():
    new = open('f_count.txt', 'w')
    new.write('0')
    new.close()

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
startButton = Button(win, image = img4, font = myFont, command = photo_count)
img1 = PhotoImage(file="1button.gif")
start1Button = Button(win, image=img1, command = photo_count)

startButton.pack(side = LEFT,padx=20)
start1Button.pack(side = RIGHT, padx=20)

mainloop()

      
