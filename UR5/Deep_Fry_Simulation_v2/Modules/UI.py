# UI.py displays crucial information about the state of the baskets in any terminal console.
# It should be noted that the external colorama library does not work in certain Windows 10 command prompts.

import time
from colorama import Fore, Style
import os
import globalvariables as g

def displayTimers():
    while True:

        #Calculating time left to shake, given that a shake occurs every 60 seconds for a total of 3 times
        b1shake_left = round(80.0 - (g.t1.endTime - g.t1.startTime))
        b2shake_left = round(80.0 - (g.t2.endTime - g.t2.startTime))
        b3shake_left = round(80.0 - (g.t3.endTime - g.t3.startTime))
        b4shake_left = round(80.0 - (g.t4.endTime - g.t4.startTime))

        #Printing out timers based on: until next shake // until completion // completed (?)
        t1Display(b1shake_left)
        t2Display(b2shake_left)
        t3Display(b3shake_left)
        t4Display(b4shake_left)

        time.sleep(3) #Refreshes every 3 seconds
        os.system('cls') #clearing the terminal console screen constantly so there's no need to scroll

#The below functions display, based on the table #, the following information:
    #Basket number identifier, type of chicken that is cooking, seconds until next shake, number of shakes left
    #Or, if NumOfShakes == 3, seconds until completion
    #Or, if completed, displays a phrase indicating so

def t1Display(b1shake_left):
    typeOfChicken = g.tableArr[0].type
    if (b1shake_left > 1000): #Accounting for the 'time glitch' where displayed time >>>> 1000
        print("Basket 1:  is empty.")

    elif (g.tableArr[0].empty == False):
        t1ShakesLeft = 3 - g.t1NumOfShakes
        if (g.t1NumOfShakes != 3):
            print("Basket 1:", Fore.GREEN + Style.BRIGHT + "[" + typeOfChicken + "]", b1shake_left, "seconds left to next shake.", 
            t1ShakesLeft, Fore.GREEN + "shake(s) left.", Style.RESET_ALL)
        elif (g.t1NumOfShakes == 3):
            if (b1shake_left <= 0):
                print("Basket 1:", Fore.CYAN + Style.BRIGHT + "[" + typeOfChicken + "]", "completed.", Style.RESET_ALL)
            else:
                print("Basket 1:", Fore.YELLOW + Style.BRIGHT + "[" + typeOfChicken + "]", b1shake_left, "seconds until completion."
                , Style.RESET_ALL)

    else:
        print("Basket 1:  is empty.")

def t2Display(b2shake_left):
    typeOfChicken = g.tableArr[1].type
    if (b2shake_left > 1000):
        print("Basket 2:  is empty.")

    elif (g.tableArr[1].empty == False):
        t2ShakesLeft = 3 - g.t2NumOfShakes
        if (g.t2NumOfShakes != 3):
            print("Basket 2:", Fore.GREEN + Style.BRIGHT + "[" + typeOfChicken + "]", b2shake_left, "seconds left to next shake.", 
            t2ShakesLeft, Fore.GREEN + "shake(s) left.", Style.RESET_ALL)
        elif (g.t2NumOfShakes == 3):
            if (b2shake_left <= 0):
                print("Basket 2:", Fore.CYAN + Style.BRIGHT + "[" + typeOfChicken + "]", "completed.", Style.RESET_ALL)
            else:
                print("Basket 2:", Fore.YELLOW + Style.BRIGHT + "[" + typeOfChicken + "]", b2shake_left, "seconds until completion."
                , Style.RESET_ALL)

    else:
        print("Basket 2:  is empty.")

def t3Display(b3shake_left):
    typeOfChicken = g.tableArr[2].type
    if (b3shake_left > 1000):
        print("Basket 3:  is empty.")

    elif (g.tableArr[2].empty == False):
        t3ShakesLeft = 3 - g.t3NumOfShakes
        if (g.t3NumOfShakes != 3):
            print("Basket 3:", Fore.GREEN + Style.BRIGHT + "[" + typeOfChicken + "]", b3shake_left, "seconds left to next shake.", 
            t3ShakesLeft, Fore.GREEN + "shake(s) left.", Style.RESET_ALL)
        elif (g.t3NumOfShakes == 3):
            if (b3shake_left <= 0):
                print("Basket 3:", Fore.CYAN + Style.BRIGHT + "[" + typeOfChicken + "]", "completed.", Style.RESET_ALL)
            else:
                print("Basket 3:", Fore.YELLOW + Style.BRIGHT + "[" + typeOfChicken + "]", b3shake_left, "seconds until completion."
                , Style.RESET_ALL)

    else:
        print("Basket 3:  is empty.")

def t4Display(b4shake_left):
    typeOfChicken = g.tableArr[3].type
    if (b4shake_left > 1000):
        print("Basket 4:  is empty.")

    elif (g.tableArr[3].empty == False):
        t4ShakesLeft = 3 - g.t4NumOfShakes
        if (g.t4NumOfShakes != 3):
            print("Basket 4:", Fore.GREEN + Style.BRIGHT + "[" + typeOfChicken + "]", b4shake_left, "seconds left to next shake.",
            t4ShakesLeft, Fore.GREEN + "shake(s) left.", Style.RESET_ALL)
        elif (g.t4NumOfShakes == 3):
            if (b4shake_left <= 0):
                print("Basket 4:", Fore.CYAN + Style.BRIGHT + "[" + typeOfChicken + "]", "completed.", Style.RESET_ALL)
            else:
                print("Basket 4:", Fore.YELLOW + Style.BRIGHT + "[" + typeOfChicken + "]", b4shake_left, "seconds until completion."
                , Style.RESET_ALL)

    else:
        print("Basket 4:  is empty.")

