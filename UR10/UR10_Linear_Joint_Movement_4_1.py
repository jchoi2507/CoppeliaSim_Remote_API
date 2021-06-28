# 6/8/2021 Jacob Choi

# To include in lua script in Coppelia software:
# simRemoteApi.start(19999)

import sim
import matplotlib.pyplot
import numpy as np
import time
import sys

sim.simxFinish(-1)  # Ends any existing communication threads
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Parameters: Server IP, Port #,


# boolean wait-until-connected
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

# Initializing + Calling Functions
joint_handle_array = []  # List of joint handles
PI = np.pi

# Initializes joint_handle_array with actual handle values -- RUN ONCE
def handle_array():
    for i in range(6):
        errorCode, joint_handle = sim.simxGetObjectHandle(clientID, "UR10_joint" + str(i + 1),
                                                          sim.simx_opmode_blocking)  # change operation mode if it doesn't work
        joint_handle_array.append(joint_handle)

## MOVE L PYTHON VERSION (This function moves the target dummy to the desired target coordinates)

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

# Helper function
def determine_if_false(string):
    if string == "quit":
        sys.exit()

# Initializing arrays of joint handles, target dummy, and final position list
handle_array()
errorCode, target = sim.simxGetObjectHandle(clientID, 'target', sim.simx_opmode_blocking)
final_position = [] # [x, y, z, alpha, beta, gamma]

# Actually running the program
print("'quit' to exit\n")

while True:
    m1 = input("Enter x coordinate\n")
    determine_if_false(m1)
    final_position.append(float(m1))
    m2 = input("Enter y coordinate\n")
    determine_if_false(m2)
    final_position.append(float(m2))
    m3 = input("Enter z coordinate\n")
    determine_if_false(m3)
    final_position.append(float(m3))
    m4 = input("Enter alpha value\n")
    determine_if_false(m4)
    final_position.append(float(m4))
    m5 = input("Enter beta value\n")
    determine_if_false(m5)
    final_position.append(float(m5))
    m6 = input("Enter gamma value\n")
    determine_if_false(m6)
    final_position.append(float(m6))

    move_L(clientID, target, final_position, 2)
    final_position.clear()
    print("--------------------------------------")
    time.sleep(3)
