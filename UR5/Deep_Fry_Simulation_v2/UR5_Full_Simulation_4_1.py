# 7/5/2021 Jacob Choi

# To include in lua script in Coppelia software:
# simRemoteApi.start(19999)

                ## Remote API connection ##

import sys
import time
from colorama import Fore, Style, Back
from tkinter import *

import basket # Basket functions module
import globalvariables as g # Global variables module
import gripper as grip # Gripper funcitons module

# Prints out a successful/unsuccessful connection message
def connectionMessage(clientid):
    if clientid != -1:
        print("Connected to remote API server")
    else:
        print("Connection unsuccessful :(. Ensure simulation is already running.")
        sys.exit()

connectionMessage(g.clientID)

                ## Performing the deep frying actions ##

# Deep frying time: 9 minutes
def boneChicken():
    print(Fore.BLUE + "Preparing your boned chicken!")

    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)

    basket.moveBasket(1)
    time.sleep(5) #200
    basket.shakeBasket(1)
    time.sleep(5) #200
    basket.shakeBasket(1)
    time.sleep(5) #100
    basket.returnBasket(1)

    print(Fore.BLUE + "Your boned chicken is ready.")

# Deep frying time: 6 minutes
def bonelessChicken():
    print(Fore.GREEN + "Preparing your boneless chicken!")

    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)

    basket.moveBasket(2)
    time.sleep(5) #120
    basket.shakeBasket(2)
    time.sleep(5) #120
    basket.shakeBasket(2)
    time.sleep(5) #120
    basket.returnBasket(2)

    print(Fore.GREEN + "Your boneless chicken is ready.")

                ## Simple UI ##

root = Tk()

boneChickenPicture = PhotoImage(file = 'boneResizedWithText.png')
bonelessChickenPicture = PhotoImage(file = 'bonelessResizedWithText.png')

button1 = Button(root, padx = 10, pady = 10, image = boneChickenPicture,
                 command = lambda: boneChicken())
button2 = Button(root, padx = 10, pady = 10, image = bonelessChickenPicture,
                 command = lambda: bonelessChicken())

button1.pack()
button2.pack()
root.mainloop()
