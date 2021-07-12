import time
import globalvariables as g
import basket
import gripper as grip
import conveyor
import checktimers

#Performs the operation of moving the bone-chicken basket from the conveyor to the deep-fryer
def boneChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex) #Spawning a non-dynamic basket to the 'batter and breading machine' platform

    checktimers.delayIfNecessary()

    time.sleep(1)
    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2) #Opens gripper at the very beginning of moving the basket
    time.sleep(2)
    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x

#Performs the operation of moving the boneless-chicken basket from the conveyor to the deep-fryer
def bonelessChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex) #Spawning a non-dynamic basket to the 'batter and breading machine' platform

    checktimers.delayIfNecessary()

    time.sleep(1)
    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2) #Opens gripper at the very beginning of moving the basket
    time.sleep(2)
    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x
