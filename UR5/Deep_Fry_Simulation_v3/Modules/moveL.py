# moveL.py is the module for the move_L function, which is responsible for moving the actual arm.
# Credit goes to 'Mechatronics Ninja' on YouTube for providing the baseline MATLAB code, which I then translated.

import sim
import numpy as np
import time

import globalvariables as g # Global variables module

# Same exact move_L function as in the linear joint movement script for the UR10, basically sets coordinates
# for the target dummy. IK will then make the tip dummy (that is attached to the flange) to follow the target dummy
def move_L(clientid, target, target_pos, speed):
    returnCode, pos = sim.simxGetObjectPosition(clientid, target, -1, sim.simx_opmode_buffer)
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

    #Accounting for orientation
    for i in range(3):
        if (abs(target_pos[i + 3]) - orient[i] > g.PI and orient[i] < 0):
            orient[i] = orient[i] + 2 * g.PI
        elif (abs(target_pos[i + 3]) - orient[i] > g.PI and orient[i] > 0):
            orient[i] = orient[i] - 2 * g.PI

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

        #Accounting for speed (?)
        startTime = time.time()
        while ((time.time() - startTime) < (distance / (speed * samples_number))):
            time.sleep(0.01)

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
