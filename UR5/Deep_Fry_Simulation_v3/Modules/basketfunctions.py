# basketfunctions.py is a subfile of basket.py, and it contains the main 'chunk' of code that actually performs
# the basket-moving operations, whereas basket.py is a cleaner version made for the sake of readability.

import time
import sim
import threading
import moveL as mL
import gripper as grip
import globalvariables as g
import checktimers

#Moves the basket from platform -> table x
def moveBasketFunc(clientid, targetPosition, arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)

    #Moving to initial position
    mL.move_L(clientid, g.target, g.initial_pos, g.kFinal)
    time.sleep(2)
    sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)

    #Closing gripper
    grip.closeGripper(clientid)
    time.sleep(1)

    if (targetPosition == 1):
        #Moving object to deep fryer
        mL.move_L(clientid, g.target, g.b1_int_pos, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b1_int_pos_2, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b1_int_pos_3, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b1_int_pos_4, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b1_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)

        g.tableArr[0].occupy() #Table 1 is now occupied
        g.tableArr[0].startTimer() #Starting timer for table 1
        time.sleep(2)
        thread1 = threading.Thread(target=checktimers.b1checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread1.start() #Running thread

        #Moving robotic arm to the 'mutual position'--where it can now reach the other baskets
        mL.move_L(clientid, g.target, g.b1_int_pos_4, g.kFinal)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_3, g.kFinal)
        time.sleep(1)

    elif (targetPosition == 2):
        #Moving object to deep fryer
        mL.move_L(clientid, g.target, g.b2_int_pos, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b2_int_pos_2, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b2_int_pos_3, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b2_int_pos_5, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b2_int_pos_6, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b2_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)

        g.tableArr[1].occupy() #Table 2 is now occupied
        g.tableArr[1].startTimer() #Starting timer for table 2
        time.sleep(2)
        thread2 = threading.Thread(target=checktimers.b2checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread2.start() #Running thread

        mutualPositionAfter2(clientid)

    elif (targetPosition == 3):
        #Moving object to deep fryer
        mL.move_L(clientid, g.target, g.b3_int_pos, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b3_int_pos_2, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b3_int_pos_3, g.kFinal)
        time.sleep(0.5)
        #mL.move_L(clientid, g.target, g.b3_int_pos_4, g.kFinal)
        #time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b3_int_pos_5, g.kFinal)
        time.sleep(0.5)
        #mL.move_L(clientid, g.target, g.b3_int_pos_6, g.kFinal)
        #time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b3_int_pos_7, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b3_int_pos_8, g.kFinal)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b3_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)

        g.tableArr[2].occupy() #Table 3 is now occupied
        g.tableArr[2].startTimer() #Starting timer for table 3
        time.sleep(2)
        thread3 = threading.Thread(target=checktimers.b3checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread3.start() #Running thread

        mutualPositionAfter3(clientid)

    elif (targetPosition == 4):
        mL.move_L(clientid, g.target, g.b4_int_pos, g.kFinal)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_2, g.kFinal)
        time.sleep(1)
        #mL.move_L(clientid, g.target, g.b4_int_pos_3, g.kFinal)
        #time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_4, g.kFinal)
        time.sleep(1)
        #mL.move_L(clientid, g.target, g.b4_int_pos_5, g.kFinal)
        #time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_6, g.kFinal)
        time.sleep(1)
        #mL.move_L(clientid, g.target, g.b4_int_pos_7, g.kFinal)
        #time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_8, g.kFinal)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_9, g.kFinal)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)

        g.tableArr[3].occupy() #Table 4 is now occupied
        g.tableArr[3].startTimer() #Starting timer for table 4
        time.sleep(2)
        thread4 = threading.Thread(target=checktimers.b4checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread4.start() #Running thread

        mutualPositionAfter4(clientid)

#Shakes a basket, located at table x
def shakeBasketFunc(clientid, targetPosition, arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)

    if (targetPosition == 1):
        mL.move_L(clientid, g.target, g.b1_final_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        for i in range(6):
            mL.move_L(clientid, g.target, g.b1_back_pos, 2)
            time.sleep(0.8)
            mL.move_L(clientid, g.target, g.b1_final_pos, 2)

    elif (targetPosition == 2):
        mL.move_L(clientid, g.target, g.b2_final_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        for i in range(6):
            mL.move_L(clientid, g.target, g.b2_back_pos, 2)
            time.sleep(0.8)
            mL.move_L(clientid, g.target, g.b2_final_pos, 2)

    elif (targetPosition == 3):
        mL.move_L(clientid, g.target, g.b3_final_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        for i in range(6):
            mL.move_L(clientid, g.target, g.b3_back_pos, 2)
            time.sleep(0.8)
            mL.move_L(clientid, g.target, g.b3_final_pos, 2)

    elif (targetPosition == 4):
        mL.move_L(clientid, g.target, g.b4_final_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        for i in range(6):
            mL.move_L(clientid, g.target, g.b4_back_pos, 2)
            time.sleep(0.8)
            mL.move_L(clientid, g.target, g.b4_final_pos, 2)

    sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
    grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
    time.sleep(1)
    mutualPositionAfterShake(clientid)

#Returns basket to 'sink hanger' (in the scene), once basket has been shaken three times.
def returnBasketFunc(clientid, targetPosition, arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)

    if (targetPosition == 1):
        mL.move_L(clientid, g.target, g.b1_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        mL.move_L(clientid, g.target, g.b1_return_pos, g.kFinal)
        time.sleep(1.5)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(1)

    elif (targetPosition == 2):
        mL.move_L(clientid, g.target, g.b2_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        mL.move_L(clientid, g.target, g.b2_return_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(1)

    elif (targetPosition == 3):
        mL.move_L(clientid, g.target, g.b3_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        mL.move_L(clientid, g.target, g.b3_return_pos, g.kFinal)
        time.sleep(1.5)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(1)

    elif (targetPosition == 4):
        mL.move_L(clientid, g.target, g.b4_final_pos, g.kFinal)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        mL.move_L(clientid, g.target, g.b4_return_pos, g.kFinal)
        time.sleep(1.5)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(1)
    
    mutualPositionAfterShake(clientid)

#These functions reset the arm to a 'mutual' position where it can move or shake other baskets

def mutualPositionAfter2(clientid):
    mutual_pos = [-1.56, 0.81, 0.725, 0, 0, 0]
    mL.move_L(clientid, g.target, mutual_pos, g.kFinal)
    time.sleep(2)

def mutualPositionAfter3(clientid):
    mutual_pos = [-1.56, 0.97, 0.725, 0, 0, 0]
    mL.move_L(clientid, g.target, mutual_pos, g.kFinal)
    time.sleep(2)

def mutualPositionAfter4(clientid):
    mutual_pos = [-1.56, 1.17, 0.725, 0, 0, 0]
    mL.move_L(clientid, g.target, mutual_pos, g.kFinal)
    time.sleep(2)

def mutualPositionAfterShake(clientid):
    mutual_pos = [-1.56, 1.1, 0.6, 0, 0, 0]
    mutual_pos_2 = [-1.56, 1.1, 0.725, 0, 0, 0]
    mL.move_L(clientid, g.target, mutual_pos, g.kFinal)
    time.sleep(1)
    mL.move_L(clientid, g.target, mutual_pos_2, g.kFinal)
    time.sleep(1)
