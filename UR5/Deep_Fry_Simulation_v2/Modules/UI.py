import time
from colorama import Fore
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

        time.sleep(1) #Refreshes every 1 second
        os.system('cls') #clearing the terminal console screen constantly so there's no need to scroll

def t1Display(b1shake_left):
    if (g.t1NumOfShakes != 3):
        print(Fore.GREEN + "Basket 1: ", b1shake_left, Fore.GREEN + " seconds left to next shake.")
    elif (g.t1NumOfShakes == 3):
        if (b1shake_left <= 0):
            print(Fore.MAGENTA + "Basket 1: completed.")
        else:
            print(Fore.YELLOW + "Basket 1: ", b1shake_left, Fore.YELLOW + " seconds until completion.")

def t2Display(b2shake_left):
    if (g.t2NumOfShakes != 3):
        print(Fore.GREEN + "Basket 2: ", b2shake_left, Fore.GREEN + " seconds left to next shake.")
    elif (g.t2NumOfShakes == 3):
        if (b2shake_left <= 0):
            print(Fore.MAGENTA + "Basket 2: completed.")
        else:
            print(Fore.YELLOW + "Basket 2: ", b2shake_left, Fore.YELLOW + " seconds until completion.")

def t3Display(b3shake_left):
    if (g.t3NumOfShakes != 3):
        print(Fore.GREEN + "Basket 3: ", b3shake_left, Fore.GREEN + " seconds left to next shake.")
    elif (g.t3NumOfShakes == 3):
        if (b3shake_left <= 0):
            print(Fore.MAGENTA + "Basket 3: completed.")
        else:
            print(Fore.YELLOW + "Basket 3: ", b3shake_left, Fore.YELLOW + " seconds until completion.")

def t4Display(b4shake_left):
    if (g.t4NumOfShakes != 3):
        print(Fore.GREEN + "Basket 4: ", b4shake_left, Fore.GREEN + " seconds left to next shake.")
    elif (g.t4NumOfShakes == 3):
        if (b4shake_left <= 0):
            print(Fore.MAGENTA + "Basket 4: completed.")
        else:
            print(Fore.YELLOW + "Basket 4: ", b4shake_left, Fore.YELLOW + " seconds until completion.")
