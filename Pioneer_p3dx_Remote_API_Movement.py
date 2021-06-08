# 6/7/2021 Jacob Choi

# To include in lua script in Coppelia software:
# simRemoteApi.start(19999)

import sim
import matplotlib.pyplot
import numpy as np

sim.simxFinish(-1) # Ends any existing communication threads
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5) # Parameters: Server IP, Port #,
                                                                  # boolean wait-until-connected
                                                                  # boolean doNotReconnectOnceDisconnected, timeOutinMs,
                                                                  # commThreadCycleinMs (usually set as 5)

# Prints out a successful/unsuccessful connection message
def connection_message(x):
    if x != -1:
        print("Connected to remote API server")
    else:
        print("Connection unsuccessful :(")

connection_message(clientID)

                                             ## MOTORS ##

# Obtaining object handles for left and right motor handles from simulation

errorCode, left_motor_handle = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_leftMotor", sim.simx_opmode_oneshot_wait)
                                                                                  # Paramters: int clientID
                                                                                  # string objectName
                                                                                  # operationMode

errorCode, right_motor_handle = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_rightMotor", sim.simx_opmode_oneshot_wait)

# Manipulating left and right motor speeds

def left_motor_speed(left_speed):
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, left_speed, sim.simx_opmode_streaming)
                                                                                  # Paramteres: int clientID,
                                                                                  # string joint handle
                                                                                  # int target velocity
                                                                                  # operationMode

def right_motor_speed(right_speed):
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, right_speed, sim.simx_opmode_streaming)

                                        ## ULTRASONIC SENSORS ##

# Obtaining handles for ultrasonic sensor (#1) installed on the Pioneer p3dx

errorCode,ultrasonicSensor1 = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_ultrasonicSensor1",
                                                      sim.simx_opmode_oneshot_wait)

# Change operation mode to sim.simx_opmode_buffer for following calls
returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector \
    = sim.simxReadProximitySensor(clientID, ultrasonicSensor1, sim.simx_opmode_streaming)

                                        ## VISION CAMERA ##

# Obtaining handles for vision sensor camera in Coppelia
errorCode, cam_handle = sim.simxGetObjectHandle(clientID, "Vision_sensor", sim.simx_opmode_oneshot_wait)

# Change operation mode to sim.simx_opmode_buffer for following calls
returnCode, resolution, image = sim.simxGetVisionSensorImage(clientID, cam_handle, 0,
                                                             sim.simx_opmode_streaming_split+4000)

## Image Rendering ##

image_1 = np.array(image, dtype = np.uint8)
image_1.resize([resolution[0], resolution[1], 3]) # Resizing the image to a more appropriate size

matplotlib.pyplot.imshow(image_1, origin = 'lower') # Displaying the actual image of the vision sensor

matplotlib.pyplot.show() # Showing the plot on computer screen