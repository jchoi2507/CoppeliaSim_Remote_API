import time
import sim
from colorama import Fore
import threading

import globalvariables as g
import basket
import gripper as grip
import conveyor
import UI as ui

def boneChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex)
    while True:
        returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
            sim.simxReadProximitySensor(g.clientID, g.proximitySensor, sim.simx_opmode_buffer)
        if (detectionState > 0):
            time.sleep(1)
            sim.simxRemoveObject(g.clientID, detectedObjectHandle, sim.simx_opmode_blocking) # change to sim.simx_opmode_oneshot if it doesn't work
            cookBoneChicken(arrIndex, counter)

            elapsedTime = g.tableArr[counter].endTime - g.tableArr[counter].startTime
            if (elapsedTime < 65.0 and elapsedTime >= 50.0): #Accounting for multiple processes
                time.sleep(10)
            break

def bonelessChicken(arrIndex, counter):
    conveyor.initBasket(arrIndex)
    while True:
        returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
            sim.simxReadProximitySensor(g.clientID, g.proximitySensor, sim.simx_opmode_buffer)
        if (detectionState > 0):
            time.sleep(1)
            sim.simxRemoveObject(g.clientID, detectedObjectHandle, sim.simx_opmode_blocking) # change to sim.simx_opmode_oneshot if it doesn't work
            cookBonelessChicken(arrIndex, counter)

            elapsedTime = g.tableArr[counter].endTime - g.tableArr[counter].startTime
            if (elapsedTime < 65.0 and elapsedTime >= 50.0): #Accounting for multiple processes
                time.sleep(10)
            break

                ## Performing the deep frying actions ##

# Deep frying time: 9 minutes
def cookBoneChicken(arrIndex, counter):
    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)

    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x
    time.sleep(5) #200

# Deep frying time: 6 minutes
def cookBonelessChicken(arrIndex, counter):
    grip.openGripperAtStart(g.clientID, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)

    basket.moveBasket(arrIndex, counter) #Move basket from conveyor -> table x
    time.sleep(5) #120
