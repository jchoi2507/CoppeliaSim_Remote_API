import sim
import numpy as np

                ## Initialization ##

clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Server IP, Port #, boolean wait-until-connected
                                                                   # boolean doNotReconnectOnceDisconnected, timeOutinMs,
                                                                   # commThreadCycleinMs (usually set as 5)

PI = np.pi

# Obtaining appropriate handles
errorCode, target = sim.simxGetObjectHandle(clientID, 'target', sim.simx_opmode_blocking)
errorCode, j1 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active1', sim.simx_opmode_blocking)
errorCode, j2 = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_active2', sim.simx_opmode_blocking)
errorCode, p1 = sim.simxGetJointPosition(clientID, j1, sim.simx_opmode_streaming)
errorCode, p2 = sim.simxGetJointPosition(clientID, j2, sim.simx_opmode_streaming)

errorCode, basket1 = sim.simxGetObjectHandle(clientID, 'basket1', sim.simx_opmode_blocking)
errorCode, basket2 = sim.simxGetObjectHandle(clientID, 'basket2', sim.simx_opmode_blocking)
errorCode, connector = sim.simxGetObjectHandle(clientID, 'ROBOTIQ_85_attachPoint', sim.simx_opmode_blocking)

                ## Coordinates ##

# Coordinates for basket 1
b1_initial_pos = [-1.725, 0.4, 0.55, 0, 0, 0]
b1_int_pos = [-1.675, 0.4, 0.725, 0, 0, 0]
b1_int_pos_2 = [-1.475, 0.4, 0.725, 0, 0, 0]
b1_int_pos_3 = [-1.475, 0.65, 0.725, 0, 0, 0]
b1_int_pos_4 = [-1.475, 0.81, 0.725, 0, 0, 0]
b1_int_pos_5 = [-1.56, 0.81, 0.725, 0, 0, 0]
b1_final_pos = [-1.56, 0.81, 0.52, 0, 0, 0]

# Coordinates for basket 2
b2_initial_pos = [-1.725, 0.6, 0.55, 0, 0, 0]
b2_int_pos = [-1.675, 0.6, 0.725, 0, 0, 0]
b2_int_pos_2 = [-1.475, 0.6, 0.725, 0, 0, 0]
b2_int_pos_3 = [-1.475, 0.8, 0.725, 0, 0, 0]
b2_int_pos_4 = [-1.475, 0.97, 0.725, 0, 0, 0]
b2_int_pos_5 = [-1.56, 0.97, 0.725, 0, 0, 0]
b2_final_pos = [-1.56, 0.97, 0.52, 0, 0, 0]
