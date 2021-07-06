# 7/5/2021 Jacob Choi

## UR5_Full_Simulation_4_1.py is the second version of the deep fry simulation. Some differences between v1 and v2
## include:
        # More applicability to a robotic kitchen--cooking either bone or boneless chicken
            # 4 baskets instead of 2
            # Proximity sensor and pseudo-conveyor application
            # 'Infinite' basket spawning mechanism
        # Menu UI with automated backend scheduling (no direct commands)
            # Improved button interface
        # Organized modules for readability and debugging purposes

# To include in Lua script in Coppelia software:
# simRemoteApi.start(19999)

from tkinter import * # Python UI library

import globalvariables as g # Global variables module
import chickencooking as cc # Chicken-cooking functions module

g.connectionMessage(g.clientID) # Printing out a successful/unsuccessful connection message

# Incrementing counter for basket array
def incCounter():
    global counter
    counter = counter + 1

                ## Simple UI ##

countArr = ["", "0", "1", "2"]
counter = 0

root = Tk()

boneChickenPicture = PhotoImage(file='boneResizedWithText.png')
bonelessChickenPicture = PhotoImage(file='bonelessResizedWithText.png')

button1 = Button(root, padx=10, pady=10, image=boneChickenPicture,
                 command=lambda: [cc.boneChicken(countArr[counter], counter), incCounter()])
button2 = Button(root, padx=10, pady=10, image=bonelessChickenPicture,
                 command=lambda: [cc.bonelessChicken(countArr[counter], counter), incCounter()])

button1.pack()
button2.pack()

root.mainloop()

