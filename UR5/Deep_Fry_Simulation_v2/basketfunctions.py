## basketfunctions.py is a subfile of basket.py, and it contains the main 'chunk' of code that actually performs
## the basket-moving operations, whereas basket.py is a cleaner version made for the sake of readability.

import time
import sim
import threading
import moveL as mL #move_L function module
import gripper as grip
import globalvariables as g
import checktimers

def moveBasketFunc(clientid, targetPosition, arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)

    #Moving to initial position
    mL.move_L(clientid, g.target, g.initial_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)

    #Closing gripper
    grip.closeGripper(clientid)
    time.sleep(1)

    if (targetPosition == 1):
        #Moving object to deep fryer
        mL.move_L(clientid, g.target, g.b1_int_pos, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_2, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_3, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(2)

        g.tableArr[0].occupy() #Table 1 is now occupied
        g.tableArr[0].startTimer() #Starting timer for table 1
        time.sleep(2)
        thread1 = threading.Thread(target=checktimers.b1checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread1.start() #Running thread

        #Moving robotic arm to the 'mutual position'--where it can now reach the other baskets
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_3, 2)
        time.sleep(1)

    elif (targetPosition == 2):
        #Moving object to deep fryer
        mL.move_L(clientid, g.target, g.b2_int_pos, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_2, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_3, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_5, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)

        g.tableArr[1].occupy() #Table 2 is now occupied
        g.tableArr[1].startTimer() #Starting timer for table 2
        time.sleep(2)
        thread2 = threading.Thread(target=checktimers.b2checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread2.start() #Running thread

        #Moving robotic arm to the 'mutual position'--where it can now reach the other baskets
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_5, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_4, 2)
        time.sleep(1)

    elif (targetPosition == 3):
        #Moving object to deep fryer
        mL.move_L(clientid, g.target, g.b3_int_pos, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_2, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_3, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_5, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_6, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_7, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_final_pos, 2)
        time.sleep(3)

        g.tableArr[2].occupy() #Table 2 is now occupied
        g.tableArr[2].startTimer() #Starting timer for table 2
        time.sleep(2)
        thread3 = threading.Thread(target=checktimers.b3checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread3.start() #Running thread

        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_7)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b3_int_pos_6)
        time.sleep(1)

    elif (targetPosition == 4):
        mL.move_L(clientid, g.target, g.b4_int_pos, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_2, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_3, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_5, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_6, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_7, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_8, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_final_pos, 2)
        time.sleep(3)

        g.tableArr[3].occupy() #Table 2 is now occupied
        g.tableArr[3].startTimer() #Starting timer for table 2
        time.sleep(2)
        thread4 = threading.Thread(target=checktimers.b4checkTimer, args=(targetPosition, arrIndex)) #Creating a thread
        thread4.start() #Running thread

        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_8)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b4_int_pos_7)
        time.sleep(1)

def shakeBasketFunc(clientid, targetPosition, arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)
    b1_back_pos = [-1.6, 0.81, 0.52, 0, 0, 0]
    b2_back_pos = [-1.6, 0.97, 0.52, 0, 0, 0]

    if (targetPosition == 1):
        mL.move_L(clientid, g.target, g.b1_final_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        for i in range(6):
            mL.move_L(clientid, g.target, b1_back_pos, 2)
            time.sleep(0.5)
            mL.move_L(clientid, g.target, g.b1_final_pos, 2)

        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        time.sleep(1)

    elif (targetPosition == 2):
        mL.move_L(clientid, g.target, g.b2_final_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        grip.closeGripper(clientid)
        time.sleep(1)

        for i in range(6):
            mL.move_L(clientid, g.target, b2_back_pos, 2)
            time.sleep(0.5)
            mL.move_L(clientid, g.target, g.b2_final_pos, 2)

        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        time.sleep(1)

    elif (targetPosition == 3):
        time.sleep(2)
        pass
    elif (targetPosition == 4):
        time.sleep(2)
        pass

def returnBasketFunc(clientid, targetPosition, arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)
    b1_return_pos = [-1.725, 0.4, 0.552, 0, 0, 0]
    b2_return_pos = [-1.725, 0.6, 0.552, 0, 0, 0]

    if (targetPosition == 1):
        mL.move_L(clientid, g.target, g.b1_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        time.sleep(1)
        grip.closeGripper(clientid)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_3, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos_2, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b1_int_pos, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, b1_return_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        time.sleep(1)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(2)
        mL.move_L(clientid, g.target, g.b2_int_pos_3, 2)
        time.sleep(2)

    elif (targetPosition == 2):
        mL.move_L(clientid, g.target, g.b2_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientid, basketH, g.connector, True, sim.simx_opmode_blocking)
        time.sleep(1.5)
        grip.closeGripper(clientid)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_5, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_4, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_3, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos_2, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, g.b2_int_pos, 2)
        time.sleep(1)
        mL.move_L(clientid, g.target, b2_return_pos, 2)
        time.sleep(4)
        sim.simxSetObjectParent(clientid, basketH, -1, True, sim.simx_opmode_blocking)
        time.sleep(1)
        grip.gripperFunction(clientid, 0, g.j1, g.j2, g.p1, g.p2)
        time.sleep(1)

    elif (targetPosition == 3):
        pass
    elif (targetPosition == 4):
        pass
