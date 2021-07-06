import time
import sim
from colorama import Fore

import globalvariables as g
import basket
import gripper as grip
import conveyor

def boneChicken(arrIndex):
    conveyor.initBasket(arrIndex)
    while True:
        returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
            sim.simxReadProximitySensor(g.clientID, g.proximitySensor, sim.simx_opmode_buffer)
        if (detectionState > 0):
            time.sleep(1)
            sim.simxRemoveObject(g.clientID, detectedObjectHandle, sim.simx_opmode_blocking) # change to sim.simx_opmode_oneshot if it doesn't work
            cookBoneChicken(arrIndex)
            break

def bonelessChicken(arrIndex):
    conveyor.initBasket(arrIndex)
    while True:
        returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
            sim.simxReadProximitySensor(g.clientID, g.proximitySensor, sim.simx_opmode_buffer)
        if (detectionState > 0):
            time.sleep(1)
            sim.simxRemoveObject(g.clientID, detectedObjectHandle, sim.simx_opmode_blocking) # change to sim.simx_opmode_oneshot if it doesn't work
            cookBonelessChicken(arrIndex)
            break

                ## Performing the deep frying actions ##

# Deep frying time: 9 minutes
def cookBoneChicken(arrIndex):
    print(Fore.BLUE + "Preparing your boned chicken!")

    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)

    basket.moveBasket(1, arrIndex) #Move basket from table 1 -> table 2
    time.sleep(5) #200
    basket.shakeBasket(1, arrIndex) #Shake basket
    time.sleep(5) #200
    basket.shakeBasket(1, arrIndex) #Shake basket
    time.sleep(5) #100
    #basket.returnBasket(1, arrIndex) #Return basket from table 2 -> table 1

    print(Fore.BLUE + "Your boned chicken is ready.")

# Deep frying time: 6 minutes
def cookBonelessChicken(arrIndex):
    print(Fore.GREEN + "Preparing your boneless chicken!")

    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)

    basket.moveBasket(2) #Move basket from table 1 -> table 2
    time.sleep(5) #120
    basket.shakeBasket(2) #Shake basket
    time.sleep(5) #120
    basket.shakeBasket(2) #Shake basket
    time.sleep(5) #120
    #basket.returnBasket(2) #Return basket from table 2 -> table 1

    print(Fore.GREEN + "Your boneless chicken is ready.")
