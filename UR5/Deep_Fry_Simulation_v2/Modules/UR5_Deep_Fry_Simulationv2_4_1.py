# Main executable file for version 2 of the deep fry simulation
# By: Jacob Choi
# 7/5/2021

from tkinter import *
import threading
import globalvariables as g
import chickencooking as cc
import UI as ui

g.connectionMessage(g.clientID) #Printing out a successful/unsuccessful remote API connection message

#Incrementing counter to loop through the countArr array
def incCounter():
    global counter
    counter = counter + 1

#Continually displays timers for baskets
def startDisplayThread():
    tableThread = threading.Thread(target=ui.displayTimers, args=())
    tableThread.start()
    return

countArr = ["", "0", "1", "2"] #Array of appendable strings that represent the basket's ID in the CoppeliaSim scene
counter = 0

#Creating a simple UI

root = Tk()

boneChickenPicture = PhotoImage(file=r"C:\Users\LG\Desktop\DeepFrySimulationv2\boneResizedWithText.png")
bonelessChickenPicture = PhotoImage(file=r"C:\Users\LG\Desktop\DeepFrySimulationv2\bonelessResized2WithText.png")

#Creating three buttons: 1) display timers option 2) order bone chicken 3) order boneless chicken
button1 = Button(root, text="POWER ON",padx=50, pady=20, command=lambda: startDisplayThread())
button2 = Button(root, image=boneChickenPicture,
                 command=lambda: [cc.boneChicken(countArr[counter], counter), incCounter()])
button3 = Button(root, image=bonelessChickenPicture,
                 command=lambda: [cc.bonelessChicken(countArr[counter], counter), incCounter()])

button1.pack(fill="both", expand=True, padx=20, pady=20)
button2.pack(side=LEFT) #Organize the buttons
button3.pack()
root.mainloop()

