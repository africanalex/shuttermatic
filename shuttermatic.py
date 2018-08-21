#!/usr/bin/env python
#forked by Joemags
#28/08/2017

from Tkinter import *
from threading import Thread
import tkFont
import time, os, subprocess

#GPIO.setmode(GPIO.BCM)
#
#POSE_LED = 20
#WAIT_LED = 16
#
#GPIO.setup(POSE_LED, GPIO.OUT)
#GPIO.output(POSE_LED, True)
#GPIO.setup(WAIT_LED, GPIO.OUT)
#GPIO.output(WAIT_LED, False)
#GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23

#def poseLight():
#    GPIO.output(POSE_LED, True)
#    time.sleep(1.5)
#    for i in range(5):
#        GPIO.output(POSE_LED, False)
#        time.sleep(0.4)
#        GPIO.output(POSE_LED, True)
#        time.sleep(0.4)
#    for i in range(5):
#        GPIO.output(POSE_LED, False)
#        time.sleep(0.1)
#        GPIO.output(POSE_LED, True)
#        time.sleep(0.1)
#    time.sleep(3)
#    GPIO.output(POSE_LED, False)
#    
#class check_button(Thread):
#
#    def __init__(self, labelText):
#        Thread.__init__(self)
#
#    def checkloop(self):
#        while True:
#            if GPIO.input(21) == 0:
#                printerOn = int(printer_on())
#                if printerOn == 1:
#                    printCount = int(photos_taken())
#                    print printCount
#                    if printCount <= 36:
#                        print "button pushed with printer on"
#                        take1Photo(1)
#                        poseLight()
#                        time.sleep(5)
#                else:
#                    print "button pushed with printer off"
#                    take1Photo(1)
#                    poseLight()
#                    time.sleep(5)
#                    


 




def photos_taken():
    import os
    if(os.path.isfile('./settings/f_count.txt')):
        m = open('/home/booth/shuttermatic/settings/f_count.txt', 'r')
        n = int(m.read())
        m.close()
        return n

def printer_on():
    import os
    if(os.path.isfile('./settings/printer.txt')):
        m = open('/home/booth/shuttermatic/settings/printer.txt', 'r')
        n = int(m.read())
        m.close()
        return n

    
def photo_count():
    import os
    if(os.path.isfile('./settings/f_count.txt')):
        m = open('/home/booth/shuttermatic/settings/f_count.txt', 'r')
        n = int(m.read())
        m.close()
        m = open('/home/booth/shuttermatic/settings/f_count.txt', 'w')
        s = str(n + 1)
        printCount = s
        m.write(s)
        m.close()
        return s

    else:
        new = open('/home/booth/shuttermatic/settings/f_count.txt', 'w')
        new.write('1')
        new.close()
        return 1

def set_colour():
    print("colour changed ")
    res = open('/Users/alexbaxter/Projects/shuttermatic/settings/colour.txt', 'w')
    res.write('1')
    res.close()

def set_bw():
    print("colour changed ")
    res = open('/Users/alexbaxter/Projects/shuttermatic/settings/colour.txt', 'w')
    res.write('0')
    res.close()

def reset_count(num):
    print("reset was clicked ")
    def wait_t():
        print("Continue...")
        label["text"] = ""
        if num == 1:
            win.after(100, assAndPrint1)
        elif num == 4:
            win.after(100, assAndPrint)
    res = open('/home/booth/shuttermatic/settings/f_count.txt', 'w')
    res.write('0')
    res.close()
    label["text"] = "Please be patient ..."
    win.after(100, wait_t)

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
        countdown(5)
        win.after(10000, takePhoto, snap-1)
    else:
        label["text"] = "Please wait..."
#        GPIO.output(WAIT_LED, True)
        win.after(100, assAndPrint)

def take1Photo(snap):
    if snap > 0:
        countdown(5)
        win.after(10000, take1Photo, snap-1)
    else:
        label["text"] = "Please wait..."
#        GPIO.output(WAIT_LED, True)
        win.after(100, assAndPrint1)        
        
def countdown(count):
    label["text"] = count
    if count > 0:
        win.after(1000, countdown, count-1)
    else:
        label["text"] = ""
        win.after(100, callCamera)

def callCamera():
    subprocess.check_output("/home/booth/shuttermatic/boothcamera.sh", shell=True)

def assAndPrint():
    p_num = int(photo_count())
    print('Photo number ', p_num)
    subprocess.call("/home/booth/shuttermatic/assemble_and_print", shell=True)
    label["text"] = "Thanks!"
#        GPIO.output(WAIT_LED, False)
    startButton.pack(side = LEFT,padx=20)
    start1Button.pack(side = RIGHT, padx=20)
    exitButton.pack(side = BOTTOM)
    
def assAndPrint1():
    p_num = int(photo_count())
    printerOn = int(printer_on())
    print('Photo number ', p_num)
    subprocess.call("/home/booth/shuttermatic/assemble_and_print_one", shell=True)
    label["text"] = "Thanks!"
#        GPIO.output(WAIT_LED, False)
    startButton.pack(side = LEFT,padx=20)
    start1Button.pack(side = RIGHT, padx=20)
    exitButton.pack(side = BOTTOM)

def exitProgram():
    win.destroy()


win = Tk()
myFont = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")

labelText1 = StringVar()
#chk1 = check_button(labelText1)
#c1 = Thread(target=chk1.checkloop)
#c1.start()


win.title("Photobooth")
win.attributes("-fullscreen", False)
label = Label(win, font = myFont)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
label["bg"] = "orange"
win["bg"] = "orange"
colourButton = Button(win, text = "Colour", font = myFont, command = set_colour)
bwButton = Button(win, text = "Black and White", font = myFont, command = set_bw)
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram)

img4 = PhotoImage(file="4button.gif")
startButton = Button(win, image = img4, font = myFont, command = buttonClicked)
img1 = PhotoImage(file="1button.gif")
start1Button = Button(win, image=img1, command = button1Clicked)

startButton.pack(side = LEFT,padx=20)
start1Button.pack(side = RIGHT, padx=20)
exitButton.pack(side = BOTTOM)
colourButton.pack(side = TOP, padx=20)
bwButton.pack(side = TOP,padx=20)
mainloop()

      
