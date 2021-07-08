from tabulate import tabulate
import time
import os

import globalvariables as g

def displayTimers():
    totalZeroCounter = 0
    while True:
        b1shake_left = 60.0 - (g.t1.endTime - g.t1.startTime)
        b2shake_left = 60.0 - (g.t2.endTime - g.t2.startTime)
        #b3shake_left = 60.0 - (g.t3.endTime - g.t3.startTime)
        #b4shake_left = 60.0 - (g.t4.endTime - g.t4.startTime)

        if (b1shake_left <= 0.0 or b2shake_left <= 0.0):
            totalZeroCounter = totalZeroCounter + 1
            if (totalZeroCounter == 6):
                break

        print("Basket 1: ", b1shake_left, " seconds left")
        print("Basket 2: ", b2shake_left, " seconds left")
        #print("Basket 3: ", b3shake_left, " seconds left")
        #print("Basket 4: ", b4shake_left, " seconds left")
        time.sleep(1)
        os.system('cls')
