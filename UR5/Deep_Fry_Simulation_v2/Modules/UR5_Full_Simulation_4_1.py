# 7/5/2021 Jacob Choi

from tkinter import *
import threading
import globalvariables as g #Global variables module
import chickencooking as cc #Chicken-cooking functions module
import UI as ui #Timer UI module

g.connectionMessage(g.clientID) #Printing out a successful/unsuccessful remote API connection message

#Incrementing counter to loop through the countArr array
def incCounter():
    global counter
    counter = counter + 1

#Continually displays timers for baskets
def startDisplayThread():
    tableThread = threading.Thread(target=ui.displayTimers,
                                   args=())
    tableThread.start()
    return

                ## Simple UI ##

countArr = ["", "0", "1", "2"] #Array of appendable strings that represent the basket's ID in the CoppeliaSim scene
counter = 0

root = Tk()

boneChickenPicture = PhotoImage(file=r"C:\Users\LG\Desktop\DeepFrySimulationv2\boneResizedWithText.png")
bonelessChickenPicture = PhotoImage(file=r"C:\Users\LG\Desktop\DeepFrySimulationv2\bonelessResizedWithText.png")

#Creating three buttons, 1) display timers option 2) order bone chicken 3) order boneless chicken
button1 = Button(root, text="Display timers",padx=120, pady=20, command=lambda: startDisplayThread())
button2 = Button(root, image=boneChickenPicture,
                 command=lambda: [cc.boneChicken(countArr[counter], counter), incCounter()])
button3 = Button(root, image=bonelessChickenPicture,
                 command=lambda: [cc.bonelessChicken(countArr[counter], counter), incCounter()])

button1.pack()
button2.pack()
button3.pack()
root.mainloop()

                ## Simple UI ##

countArr = ["", "0", "1", "2"]
counter = 0

root = Tk()

boneChickenPicture = PhotoImage(file='boneResizedWithText.png')
bonelessChickenPicture = PhotoImage(file='bonelessResizedWithText.png')

button1 = Button(root, text="Click here to start ordering.",padx=10, pady=10, command=lambda: startDisplayThread())
button2 = Button(root, padx=10, pady=10, image=boneChickenPicture,
                 command=lambda: [cc.boneChicken(countArr[counter], counter), incCounter()])
button3 = Button(root, padx=10, pady=10, image=bonelessChickenPicture,
                 command=lambda: [cc.bonelessChicken(countArr[counter], counter), incCounter()])

button1.pack()
button2.pack()
button3.pack()

root.mainloop()
