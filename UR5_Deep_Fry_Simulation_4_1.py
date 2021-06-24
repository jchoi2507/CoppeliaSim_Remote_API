# 6/21/2021 Jacob Choi

# To include in lua script in Coppelia software:
# simRemoteApi.start(19999)

                                            ## Settings Tutorial ##

# For any confusion on:

    # Function parameters: https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm#
    # Understanding dynamic simulations: https://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm
    # Remote API connection: https://youtu.be/SQont-mTnfM?t=982
        # 'vrep' is the same as 'sim'
    # The move_L function: https://youtu.be/CVoV08T0Aqo?t=948
        # The code below is basically a Python version of his MATLAB code

# Important notes about UR5_Deep_Fry_Simulation_4_1.py:

    # Coppelia 4.1 should be installed, not the current version of 4.2. This is due to the current version not
    # supporting tip&target inverse kinematic control through remote API

    # The basket objects are STATIC, non-respondable bodies--in other words, the gripper
    # isn't actually 'gripping' them, they are floating alongside the gripper, emulating
    # an actual gripper (for gripping dynamic, respondable bodies, refer to: UR5_Pick_And_Place_4_1.py
    # in the repository).

    # Sphere object is there purely for the purpose of having the above simRemoteApi.start(19999) in its child script;
    # without that command somewhere in the scene, remote API connection is not possible. The command is not included in the
    # child script of the actual robotic arm for the sake of disabling the object's entire child script.

    # Two dummies, 'tip' and 'target'; 'tip' is a child object of the last object of the UR5 in the model hierarchy
    # 'tip' and 'target' are linked in the IK-tip-to-target mode, with an IK group + element established.
    # The 'tip' dummy has to be placed at the flange of the robotic arm, whereas the 'target' dummy can be anywhere.
    # Once simulation runs, the robotic arm should theoretically follow the 'target' dummy through IK calculations.
    # However, do be careful of positioning the target, it should be somewhere within the robot arm's reach (not too far
    # away but also not too close to avoid singularity issues)

    # All joints in the UR5 robotic arm are set to inverse kinematics mode + hybrid operation enabled.

    # The gripper is the child object of the UR5_connection object. Contrary to online tutorials, the gripper can
    # remain dynamically ENABLED as long as it's connected to the correct object. See:
    # https://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm

                            #####################################################

                ## Remote API connection ##

import sim
import matplotlib.pyplot
import numpy as np
import time
import sys

sim.simxFinish(-1)  # Ends any existing communication threads
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Server IP, Port #, boolean wait-until-connected
                                                                   # boolean doNotReconnectOnceDisconnected, timeOutinMs,
                                                                   # commThreadCycleinMs (usually set as 5)

# Prints out a successful/unsuccessful connection message
def connection_message(x):
    if x != -1:
        print("Connected to remote API server")
    else:
        print("Connection unsuccessful :(")
        sys.exit()

connection_message(clientID)

                ## Gripper functions ##

from functools import partial
from tkinter import *
root = Tk()
PI = np.pi

# Gripper function that opens/closes the gripper
def gripper_function(clientid, closing, j1, j2, p1, p2):
    errorCode, p1 = sim.simxGetJointPosition(clientid, j1, sim.simx_opmode_buffer)
    errorCode, p2 = sim.simxGetJointPosition(clientid, j2, sim.simx_opmode_buffer)

    if closing == 1:
        if p1 < (p2 - 0.008):
            sim.simxSetJointTargetVelocity(clientid, j1, -0.1, sim.simx_opmode_oneshot) #Try sim.simx_opmode_streaming if it doesn't work
            sim.simxSetJointTargetVelocity(clientid, j2, -0.4, sim.simx_opmode_oneshot)
        else:
            sim.simxSetJointTargetVelocity(clientid, j1, -0.4, sim.simx_opmode_oneshot)
            sim.simxSetJointTargetVelocity(clientid, j2, -0.4, sim.simx_opmode_oneshot)

    else:
        if p1 < p2:
            sim.simxSetJointTargetVelocity(clientid, j1, 0.4, sim.simx_opmode_oneshot)
            sim.simxSetJointTargetVelocity(clientid, j2, 0.2, sim.simx_opmode_oneshot)
        else:
            sim.simxSetJointTargetVelocity(clientid, j1, 0.2, sim.simx_opmode_oneshot)
            sim.simxSetJointTargetVelocity(clientid, j2, 0.4, sim.simx_opmode_oneshot)

# The below function will stop moving the gripper, thus achieving 'fake gripping'
def pause_gripper(clientid, j1, j2):
    sim.simxSetJointTargetVelocity(clientid, j1, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientid, j2, 0, sim.simx_opmode_oneshot)

# Simply opens the gripper at the start, as the gripper in my scene is closed at the beginning of simulation.
# Feel free to turn off if the gripper is already in an open position
def openGripperAtStart(clientid, j1, j2, p1, p2):
    errorCode, p1 = sim.simxGetJointPosition(clientid, j1, sim.simx_opmode_buffer)
    errorCode, p2 = sim.simxGetJointPosition(clientid, j2, sim.simx_opmode_buffer)

    if p1 < p2:
        sim.simxSetJointTargetVelocity(clientid, j1, 0.4, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientid, j2, 0.2, sim.simx_opmode_oneshot)
    else:
        sim.simxSetJointTargetVelocity(clientid, j1, 0.2, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientid, j2, 0.4, sim.simx_opmode_oneshot)

                ## Move_L function

# Same exact move_L function as in the linear joint movement script for the UR10, basically sets coordinates
# for the target dummy. IK will then make the tip dummy (that is attached to the flange) to follow the target dummy
def move_L(clientid, target, target_pos, speed):
    returnCode, pos = sim.simxGetObjectPosition(clientid, target, -1, sim.simx_opmode_streaming)
    returnCode, pos = sim.simxGetObjectPosition(clientid, target, -1,
                                                sim.simx_opmode_buffer)

    returnCode, orient = sim.simxGetObjectOrientation(clientid, target, -1, sim.simx_opmode_streaming)
    returnCode, orient = sim.simxGetObjectOrientation(clientid, target, -1, sim.simx_opmode_buffer)

    for i in range(3):
        pos[i] = float(pos[i])
        orient[i] = float(orient[i])

    old_pos = []
    old_orient = []
    delta_pos = []
    delta_orient = []
    intermediate_pos = [0, 0, 0]
    intermediate_orient = [0, 0, 0]
    # target_pos = [1.5, 2, 5] ## TEST

    for i in range(3):
        if abs(target_pos[i + 3]) - orient[i] > PI and orient[i] < 0:
            orient[i] = orient[i] + 2*PI
        elif abs(target_pos[i + 3]) - orient[i] > PI and orient[i] > 0:
            orient[i] = orient[i] - 2*PI

    for i in range(3):
        old_pos.append(pos[i])
        delta_pos.append(target_pos[i] - old_pos[i])
        old_orient.append(orient[i])
        delta_orient.append(target_pos[i + 3] - old_orient[i])

    distance = np.linalg.norm(delta_pos)
    samples_number = round(distance * 50)

    for i in range(samples_number):
        for j in range(3):
            intermediate_pos[j] = (old_pos[j] + (delta_pos[j] / samples_number))
            intermediate_orient[j] = (old_orient[j] + (delta_orient[j] / samples_number))

        sim.simxSetObjectPosition(clientid, target, -1, intermediate_pos, sim.simx_opmode_oneshot)
        sim.simxSetObjectOrientation(clientid, target, -1, intermediate_orient, sim.simx_opmode_oneshot)

        for k in range(3):
            old_pos[k] = intermediate_pos[k]
            old_orient[k] = intermediate_orient[k]

        for k in range(3):
            intermediate_pos[k] = 0
            intermediate_orient[k] = 0

    old_pos.clear()
    delta_pos.clear()
    intermediate_pos.clear()

                ## Initializing

# Obtaining appropriate handles
errorCode, target = sim.simxGetObjectHandle(clientID, 'target', sim.simx_opmode_blocking)
errorCode, j1 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active1', sim.simx_opmode_blocking)
errorCode, j2 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active2', sim.simx_opmode_blocking)
errorCode, p1 = sim.simxGetJointPosition(clientID, j1, sim.simx_opmode_streaming)
errorCode, p2 = sim.simxGetJointPosition(clientID, j2, sim.simx_opmode_streaming)

# Coordinates for basket 1
b1_initial_pos = [-1.725, 0.4, 0.55, 0, 0, 0]
b1_int_pos = [-1.675, 0.4, 0.725, 0, 0, 0]
b1_int_pos_2 = [-1.475, 0.4, 0.725, 0, 0, 0]
b1_int_pos_3 = [-1.475, 0.65, 0.725, 0, 0, 0]
b1_int_pos_4 = [-1.475, 0.81, 0.725, 0, 0, 0]
b1_int_pos_5 = [-1.56, 0.81, 0.725, 0, 0, 0]
b1_final_pos = [-1.56, 0.81, 0.52, 0, 0, 0]

b1_b2_transition_pos = [-1.85, 0.55, 0.6, 0, 0, 0]

# Coordinates for basket 2
b2_initial_pos = [-1.725, 0.6, 0.55, 0, 0, 0]
b2_int_pos = [-1.675, 0.6, 0.725, 0, 0, 0]
b2_int_pos_2 = [-1.475, 0.6, 0.725, 0, 0, 0]
b2_int_pos_3 = [-1.475, 0.8, 0.725, 0, 0, 0]
b2_int_pos_4 = [-1.475, 0.97, 0.725, 0, 0, 0]
b2_int_pos_5 = [-1.56, 0.97, 0.725, 0, 0, 0]
b2_final_pos = [-1.56, 0.97, 0.52, 0, 0, 0]

errorCode, basket1 = sim.simxGetObjectHandle(clientID, 'basket1', sim.simx_opmode_blocking)
errorCode, basket2 = sim.simxGetObjectHandle(clientID, 'basket2', sim.simx_opmode_blocking)
errorCode, connector = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_attachPoint', sim.simx_opmode_blocking)

                ## Basket-moving functions

# Function that perform the movements of the cuboids/baskets
def moveBasket(basket_number):

    if basket_number == 1:
        # Moving to initial position
        move_L(clientID, target, b1_initial_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket1, connector, True, sim.simx_opmode_blocking)

        # Closing gripper
        gripper_function(clientID, 1, j1, j2, p1, p2)
        time.sleep(0.85)
        pause_gripper(clientID, j1, j2)
        time.sleep(1)

        # Moving object to second table
        move_L(clientID, target, b1_int_pos, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_2, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_3, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_4, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_5, 2)
        time.sleep(1)
        move_L(clientID, target, b1_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket1, -1, True, sim.simx_opmode_blocking)
        gripper_function(clientID, 0, j1, j2, p1, p2)

        # Moving robotic arm back to first table, ready to move basket #2
        # move_L(clientID, target, b1_final_pos_2, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_5, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_4, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_3, 2)
        time.sleep(1)

    elif basket_number == 2:
        # Moving to initial position
        move_L(clientID, target, b2_initial_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket2, connector, True, sim.simx_opmode_blocking)

        # Closing gripper
        gripper_function(clientID, 1, j1, j2, p1, p2)
        time.sleep(0.85)
        pause_gripper(clientID, j1, j2)
        time.sleep(2)

        # Moving object to second table
        move_L(clientID, target, b2_int_pos, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_2, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_3, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_4, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_5, 2)
        time.sleep(1)
        move_L(clientID, target, b2_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket2, -1, True, sim.simx_opmode_blocking)
        gripper_function(clientID, 0, j1, j2, p1, p2)

        # Moving robotic arm back to original position
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_5, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_4, 2)
        time.sleep(1)

def shakeBasket(basket_number):

    b1_back_pos = [-1.6, 0.81, 0.52, 0, 0, 0]
    b2_back_pos = [-1.6, 0.97, 0.52, 0, 0, 0]

    if basket_number == 1:
        move_L(clientID, target, b1_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket1, connector, True, sim.simx_opmode_blocking)
        gripper_function(clientID, 1, j1, j2, p1, p2)
        time.sleep(0.85)
        pause_gripper(clientID, j1, j2)
        time.sleep(1)

        for i in range(6):
            move_L(clientID, target, b1_back_pos, 2)
            time.sleep(0.5)
            move_L(clientID, target, b1_final_pos, 2)

    elif basket_number == 2:
        move_L(clientID, target, b2_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket2, connector, True, sim.simx_opmode_blocking)
        gripper_function(clientID, 1, j1, j2, p1, p2)
        time.sleep(0.85)
        pause_gripper(clientID, j1, j2)
        time.sleep(1)

        for i in range(6):
            move_L(clientID, target, b2_back_pos, 2)
            time.sleep(0.5)
            move_L(clientID, target, b2_final_pos, 2)

    time.sleep(2)
    sim.simxSetObjectParent(clientID, basket1, -1, True, sim.simx_opmode_blocking)
    sim.simxSetObjectParent(clientID, basket2, -1, True, sim.simx_opmode_blocking)
    gripper_function(clientID, 0, j1, j2, p1, p2)
    time.sleep(2)

def moveBack(basket_number):

    b1_return_pos = [-1.725, 0.4, 0.552, 0, 0, 0]
    b2_return_pos = [-1.725, 0.6, 0.552, 0, 0, 0]

    if basket_number == 1:
        move_L(clientID, target, b1_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket1, connector, True, sim.simx_opmode_blocking)
        time.sleep(1)
        gripper_function(clientID, 1, j1, j2, p1, p2)
        time.sleep(0.85)
        pause_gripper(clientID, j1, j2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_5, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_4, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_3, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos_2, 2)
        time.sleep(1)
        move_L(clientID, target, b1_int_pos, 2)
        time.sleep(1)
        move_L(clientID, target, b1_return_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientID, basket1, -1, True, sim.simx_opmode_blocking)
        time.sleep(1)
        gripper_function(clientID, 0, j1, j2, p1, p2)
        time.sleep(2)
        move_L(clientID, target, b2_int_pos_3, 2)
        time.sleep(2)

    elif basket_number == 2:
        move_L(clientID, target, b2_final_pos, 2)
        time.sleep(3)
        sim.simxSetObjectParent(clientID, basket2, connector, True, sim.simx_opmode_blocking)
        time.sleep(1.5)
        gripper_function(clientID, 1, j1, j2, p1, p2)
        time.sleep(0.85)
        pause_gripper(clientID, j1, j2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_5, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_4, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_3, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos_2, 2)
        time.sleep(1)
        move_L(clientID, target, b2_int_pos, 2)
        time.sleep(1)
        move_L(clientID, target, b2_return_pos, 2)
        time.sleep(2)
        sim.simxSetObjectParent(clientID, basket2, -1, True, sim.simx_opmode_blocking)
        time.sleep(1)
        gripper_function(clientID, 0, j1, j2, p1, p2)
        time.sleep(1)

                ## Creating a simple GUI

openGripperAtStart(clientID, j1, j2, p1, p2) # Opening the gripper at the beginning of simulation

button1 = Button(root, text = "Move Basket 1", padx = 50, pady = 50, command = lambda: moveBasket(1))
button2 = Button(root, text = "Shake Basket 1", padx = 50, pady = 50, command = lambda: shakeBasket(1))
button3 = Button(root, text = "Return Basket 1", padx = 50, pady = 50, command = lambda: moveBack(1))

button4 = Button(root, text = "Move Basket 2", padx = 50, pady = 50, command = lambda: moveBasket(2))
button5 = Button(root, text = "Shake Basket 2", padx = 50, pady = 50, command = lambda: shakeBasket(2))
button6 = Button(root, text = "Return Basket 2", padx = 50, pady = 50, command = lambda: moveBack(2))

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()

root.mainloop()
