import time
import os
import globalvariables as g

def displayTimers():
    totalZeroCounter = 0
    while True:

        if (60.0 - (g.t1.endTime - g.t1.startTime) > 61.0 or 60.0 - (g.t2.endTime - g.t2.startTime) > 61.0): #Accounting for the time 'glitch'
            time.sleep(1)
        else:
            pass
        
        #Calculating time left to shake, given that a shake occurs every 60 seconds for a total of 3 times
        b1shake_left = 60.0 - (g.t1.endTime - g.t1.startTime)
        b2shake_left = 60.0 - (g.t2.endTime - g.t2.startTime)
        b3shake_left = 60.0 - (g.t3.endTime - g.t3.startTime)
        b4shake_left = 60.0 - (g.t4.endTime - g.t4.startTime)

        #if (b1shake_left <= 0.0 or b2shake_left <= 0.0):
            #totalZeroCounter = totalZeroCounter + 1
            #if (totalZeroCounter == 6): #Change to 9, 12 to account for 3, 4 baskets
                #break

        print("Basket 1: ", b1shake_left, " seconds left to next shake.")
        print("Basket 2: ", b2shake_left, " seconds left to next shake.")
        print("Basket 3: ", b3shake_left, " seconds left to next shake.")
        print("Basket 4: ", b4shake_left, " seconds left to next shake.")
        time.sleep(1)

        os.system('cls') #clearing the terminal console constantly so that timers are updated without constantly printing times
