## globalvariables.py is the module that contains the global variables for other files to access.
## Additionally, all initializations (clientID, handles, coordinates, etc, etc.) are configured here.

import sys
import sim
import numpy as np
import time
from tabulate import tabulate # Python table library

                ## Classes ##

class Table:
    def __init__(self):
        self.empty = True
        self.startTime = 0
        self.endTime = 0

    def occupy(self):
        self.empty = False

    def vacate(self):
        self.empty = True

    def startTimer(self):
        self.startTime = time.time()

    def endTimer(self):
        self.endTime = time.time()

t1 = Table()
t2 = Table()
t3 = Table()
t4 = Table()
tableArr = [t1, t2, t3, t4]

                ## Initialization ##

clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Server IP, Port #, boolean wait-until-connected
                                                                   # boolean doNotReconnectOnceDisconnected, timeOutinMs,
                                                                   # commThreadCycleinMs (usually set as 5)

def connectionMessage(clientid):
    if clientid != -1:
        print("Connected to remote API server")
    else:
        print("Connection unsuccessful :(. Ensure simulation is already running + correct files in directory.")
        sys.exit()

PI = np.pi

# Obtaining appropriate handles
errorCode, target = sim.simxGetObjectHandle(clientID, 'target', sim.simx_opmode_blocking) #target dummy
errorCode, j1 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active1', sim.simx_opmode_blocking) #gripper joint 1
errorCode, j2 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active2', sim.simx_opmode_blocking) #gripper joint 2
errorCode, connector = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_attachPoint',
                                               sim.simx_opmode_blocking) #gripper connect point
errorCode, proximitySensor = sim.simxGetObjectHandle(clientID, 'Proximity_sensor',
                                                     sim.simx_opmode_blocking) #proximity sensor

returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
    sim.simxReadProximitySensor(clientID, proximitySensor, sim.simx_opmode_streaming) #Initializing proximity sensor

# Obtaining joint positions for the gripper to close & open
errorCode, p1 = sim.simxGetJointPosition(clientID, j1, sim.simx_opmode_streaming)
errorCode, p2 = sim.simxGetJointPosition(clientID, j2, sim.simx_opmode_streaming)

                ## Coordinates ##

# Coordinates for basket 1
b1_initial_pos = [-1.63, 0.59, 0.675, 0, 0, 0] # [x, y, z, alpha, beta, gamma]
b1_int_pos = [-1.63, 0.59, 0.725, 0, 0, 0]
b1_int_pos_2 = [-1.475, 0.65, 0.725, 0, 0, 0]
b1_int_pos_3 = [-1.475, 0.81, 0.725, 0, 0, 0]
b1_int_pos_4 = [-1.56, 0.81, 0.725, 0, 0, 0]
b1_final_pos = [-1.56, 0.81, 0.52, 0, 0, 0]

# Coordinates for basket 2
b2_initial_pos = [-1.725, 0.6, 0.55, 0, 0, 0]
b2_int_pos = [-1.675, 0.6, 0.725, 0, 0, 0]
b2_int_pos_2 = [-1.475, 0.6, 0.725, 0, 0, 0]
b2_int_pos_3 = [-1.475, 0.8, 0.725, 0, 0, 0]
b2_int_pos_4 = [-1.475, 0.97, 0.725, 0, 0, 0]
b2_int_pos_5 = [-1.56, 0.97, 0.725, 0, 0, 0]
b2_final_pos = [-1.56, 0.97, 0.52, 0, 0, 0]

