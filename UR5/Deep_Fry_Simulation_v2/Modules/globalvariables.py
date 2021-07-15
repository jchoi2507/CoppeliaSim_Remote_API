# globalvariables.py is the module that contains the global variables for other files to access.
# Additionally, all initializations (clientID, handles, coordinates, etc, etc.) are configured here.

import sys
import sim
import numpy as np
import time

                ## Classes ##

#Table class that represents one section of one deep-fryer (in the CoppeliaSim scene, this is one-half of one of the red tables)
class Table:

    #Constructor method
    def __init__(self):
        self.empty = True #boolean empty or not
        self.startTime = 0 #time at shake start
        self.endTime = 0 #time at shake end
        self.type = "" #type of chicken (bone or boneless)

    #Occupy method
    def occupy(self):
        self.empty = False

    #Empty method
    def vacate(self):
        self.empty = True

    #Starting the timer at shake start method
    def startTimer(self):
        self.startTime = time.time()

    #Ending the timer at shake end method
    def endTimer(self):
        self.endTime = time.time()

t1 = Table()
t2 = Table()
t3 = Table()
t4 = Table()
tableArr = [t1, t2, t3, t4] #Table array representing the four available spaces in the deep fryer system

#Global variables representing how many shakes each basket has gone through
t1NumOfShakes = 0
t2NumOfShakes = 0
t3NumOfShakes = 0
t4NumOfShakes = 0

                ## Initialization ##

clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  #Server IP, Port num, boolean wait-until-connected
                                                                   #boolean doNotReconnectOnceDisconnected, timeOutinMs,
                                                                   #commThreadCycleinMs (usually set as 5)

def connectionMessage(clientid):
    if (clientid != -1):
        print("Connected to remote API server")
    else:
        print("Connection unsuccessful :(. Ensure simulation is already running + correct files in directory.")
        sys.exit()

PI = np.pi #For move_L calculations

#Obtaining appropriate handles
errorCode, target = sim.simxGetObjectHandle(clientID, 'target', sim.simx_opmode_blocking) #target dummy
errorCode, j1 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active1', sim.simx_opmode_blocking) #gripper joint 1
errorCode, j2 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active2', sim.simx_opmode_blocking) #gripper joint 2
errorCode, connector = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_attachPoint',
                                               sim.simx_opmode_blocking) #gripper connect point

#Obtaining joint positions for the gripper to close & open
errorCode, p1 = sim.simxGetJointPosition(clientID, j1, sim.simx_opmode_streaming)
errorCode, p2 = sim.simxGetJointPosition(clientID, j2, sim.simx_opmode_streaming)

                ## Coordinates ##

#Initial + spawn point coordinates
initial_pos = [-1.63, 0.59, 0.675, 0, 0, 0] #[x, y, z, alpha, beta, gamma]
basket_spawn = [-1.788, 0.5912, 0.6138] #[x, y, z]

#Basket-shaking coordinates
b1_back_pos = [-1.6, 0.81, 0.52, 0, 0, 0]
b2_back_pos = [-1.6, 0.97, 0.52, 0, 0, 0]
b3_back_pos = [-1.6, 1.17, 0.52, 0, 0, 0]
b4_back_pos = [-1.6, 1.3, 0.52, 0, 0, 0]

#Basket-returning coordinates
b1_return_pos = [-1.64, 0.88, 0.68, 0, 0, 0]
b2_return_pos = [-1.64, 1, 0.68, 0, 0, 0]
b3_return_pos = [-1.64, 1.16, 0.68, 0, 0, 0]
b4_return_pos = [-1.64, 1.27, 0.68, 0, 0, 0]

#Basket-moving coordinates for basket 1
b1_int_pos = [-1.63, 0.59, 0.725, 0, 0, 0]
b1_int_pos_2 = [-1.475, 0.65, 0.725, 0, 0, 0]
b1_int_pos_3 = [-1.475, 0.81, 0.725, 0, 0, 0]
b1_int_pos_4 = [-1.56, 0.81, 0.725, 0, 0, 0]
b1_final_pos = [-1.56, 0.81, 0.52, 0, 0, 0]

#Basket-moving coordinates for basket 2
b2_int_pos = [-1.63, 0.59, 0.725, 0, 0, 0]
b2_int_pos_2 = [-1.475, 0.65, 0.725, 0, 0, 0]
b2_int_pos_3 = [-1.475, 0.8, 0.725, 0, 0, 0]
b2_int_pos_4 = [-1.475, 0.88, 0.725, 0, 0, 0]
b2_int_pos_5 = [-1.475, 0.97, 0.725, 0, 0, 0]
b2_int_pos_6 = [-1.56, 0.97, 0.725, 0, 0, 0]
b2_final_pos = [-1.56, 0.97, 0.52, 0, 0, 0]

#Basket-moving coordinates for basket 3
b3_int_pos = [-1.63, 0.59, 0.725, 0, 0, 0]
b3_int_pos_2 = [-1.475, 0.65, 0.725, 0, 0, 0]
b3_int_pos_3 = [-1.475, 0.8, 0.725, 0, 0, 0]
b3_int_pos_4 = [-1.475, 0.9, 0.725, 0, 0, 0]
b3_int_pos_5 = [-1.475, 1.0, 0.725, 0, 0, 0]
b3_int_pos_6 = [-1.475, 1.1, 0.725, 0, 0, 0]
b3_int_pos_7 = [-1.475, 1.17, 0.725, 0, 0, 0]
b3_int_pos_8 = [-1.56, 1.17, 0.725, 0, 0, 0]
b3_final_pos = [-1.56, 1.17, 0.52, 0, 0, 0]

#Basket-moving coordinates for basket 4
b4_int_pos = [-1.63, 0.59, 0.725, 0, 0, 0]
b4_int_pos_2 = [-1.475, 0.65, 0.725, 0, 0, 0]
b4_int_pos_3 = [-1.475, 0.8, 0.725, 0, 0, 0]
b4_int_pos_4 = [-1.475, 0.9, 0.725, 0, 0, 0]
b4_int_pos_5 = [-1.475, 1.0, 0.725, 0, 0, 0]
b4_int_pos_6 = [-1.475, 1.1, 0.725, 0, 0, 0]
b4_int_pos_7 = [-1.475, 1.17, 0.725, 0, 0, 0]
b4_int_pos_8 = [-1.475, 1.3, 0.725, 0, 0, 0]
b4_int_pos_9 = [-1.56, 1.3, 0.725, 0, 0, 0]
b4_final_pos = [-1.56, 1.3, 0.52, 0, 0, 0]
