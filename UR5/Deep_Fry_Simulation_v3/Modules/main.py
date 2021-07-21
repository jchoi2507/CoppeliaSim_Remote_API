# Main executable file for version 3 of the deep fry simulation
# By: Jacob Choi
# 7/5/2021

#Make sure these files are in your workspace directory:
    #sim.py
    #simConst.py
    #remoteApi.dll (Windows); remoteApi.dylib (Mac)

from tkinter import *
import threading
import globalvariables as g
import chickencooking as cc
import UI as ui
import UI2 as ui2
import datetime

g.connectionMessage(g.clientID) #Printing out a successful/unsuccessful remote API connection message

#Incrementing counter to loop through the countArr array
def incCounter():
    global counter
    counter = counter + 1

#Allow user to control speeds based on input (range: 0.1 m/s = 100 mm/s < x < 100 m/s = 100000 mm/s)
def speedInput():
    g.kFinal = (int(entryButton.get()) / 1000)

def updateLabel():
    b1shake_left = round(80.0 - (g.t1.endTime - g.t1.startTime))
    b2shake_left = round(80.0 - (g.t2.endTime - g.t2.startTime))
    b3shake_left = round(80.0 - (g.t3.endTime - g.t3.startTime))
    b4shake_left = round(80.0 - (g.t4.endTime - g.t4.startTime))

    time1 = ui2.t1Display(b1shake_left)
    time2 = ui2.t2Display(b2shake_left)
    time3 = ui2.t3Display(b3shake_left)
    time4 = ui2.t4Display(b4shake_left)

    testLabel.config(text=time1)
    testLabel2.config(text=time2)
    testLabel3.config(text=time3)
    testLabel4.config(text=time4)

    root.after(1000, updateLabel)

countArr = ["", "0", "1", "2"] #Array of appendable strings that represent the basket's ID in the CoppeliaSim scene
counter = 0

#Creating a simple UI
root = Tk() #Root for menu, timers UI, and speed input

#Change the following file directories based on wherever you stored your images
boneChickenPicture = \
    PhotoImage(file=r"/Users/jacobchoi/Desktop/ProgrammingDirectory/PythonFiles/boneResizedWithText.png")
bonelessChickenPicture = \
    PhotoImage(file=r"/Users/jacobchoi/Desktop/ProgrammingDirectory/PythonFiles/bonelessResized2WithText.png")

#Creating widgets
button1 = Button(root, image=boneChickenPicture,
                 command=lambda: [cc.boneChicken(countArr[counter], counter), incCounter()])
button2 = Button(root, image=bonelessChickenPicture,
                 command=lambda: [cc.bonelessChicken(countArr[counter], counter), incCounter()])

testLabel = Label(root)
testLabel2 = Label(root)
testLabel3 = Label(root)
testLabel4 = Label(root)

speedLabel = Label(root, text="Robotic arm speed (mm/s): ")
entryButton = Entry(root)
enterButton = Button(root, text="Enter", command=lambda: speedInput())

#Packing widgets
speedLabel.pack(side=TOP)
entryButton.pack(side=TOP)
enterButton.pack(pady=(0, 30))
testLabel.pack()
testLabel2.pack()
testLabel3.pack()
testLabel4.pack(pady=(0, 30))

updateLabel() #Calling the function that constantly updates the basket timer widget

button1.pack(side=LEFT) #Organize the buttons
button2.pack()

root.mainloop()
