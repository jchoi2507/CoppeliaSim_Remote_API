# chickencooking.py acts as the link between the button interface and actual commands. It performs the spawning of the basket,
# initialization of the appropriate basket/table class, and calls the move function for the basket.

import time
import globalvariables as g
import basket
import gripper as grip
import conveyor
import checktimers

#Performs the operation of moving the bone-chicken basket from the conveyor to the deep-fryer
def boneChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex) #Spawning a non-dynamic basket to the 'batter and breading machine' platform
    g.tableArr[counter].type = "BONE"
    checktimers.delayIfNecessary() #Accounting for multiple baskets in the system

    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2) #Opens gripper at the very beginning of moving the basket
    time.sleep(2)
    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x

#Performs the operation of moving the boneless-chicken basket from the conveyor to the deep-fryer
def bonelessChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex)
    g.tableArr[counter].type = "BONELESS"
    checktimers.delayIfNecessary()

    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)
    basket.moveBasket(arrIndex, counter) 
