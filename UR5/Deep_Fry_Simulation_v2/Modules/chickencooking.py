import time
import sim
import globalvariables as g
import basket #Refined version of the basketfunctions.py module
import gripper as grip #Gripper functions module
import conveyor #Conveyor functions module
import checktimers #Threaded functions to check basket-shaking timer module

#Performs the operation of moving the basket from the conveyor to the deep-fryer
def boneChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex) #Attaching a non-dynamic basket to the dynamic, respondable, invisible cuboid shape
    while True:

        checktimers.delayIfNecessary()       

        time.sleep(1)
        cookBoneChicken(arrIndex, counter)
        break

        #elapsedTime = g.tableArr[counter].endTime - g.tableArr[counter].startTime

#Performs the operation of moving the basket from the conveyor to the deep-fryer
def bonelessChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex) #Attaching a non-dynamic basket to the dynamic, respondable, invisible cuboid shape
    while True:

        checktimers.delayIfNecessary()

        time.sleep(1)
        cookBonelessChicken(arrIndex, counter)
        break

        #elapsedTime = g.tableArr[counter].endTime - g.tableArr[counter].startTime

# Deep frying time: 9 minutes
def cookBoneChicken(arrIndex, counter):
    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2) #Opens gripper at the very beginning of moving the basket
    time.sleep(2)

    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x
    time.sleep(5) #200

# Deep frying time: 6 minutes
def cookBonelessChicken(arrIndex, counter):
    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2) #Opens gripper at the very beginning of moving the basket
    time.sleep(2)

    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x
    time.sleep(5) #120
