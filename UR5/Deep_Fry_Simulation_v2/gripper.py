import sim

                ## Gripper functions ##

# Gripper function that opens/closes the gripper
def gripper_function(clientid, closing, j1, j2, p1, p2):

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
def openGripperAtStart(clientid, j1, j2, p1, p2):

    if p1 < p2:
        sim.simxSetJointTargetVelocity(clientid, j1, 0.4, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientid, j2, 0.2, sim.simx_opmode_oneshot)
    else:
        sim.simxSetJointTargetVelocity(clientid, j1, 0.2, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientid, j2, 0.4, sim.simx_opmode_oneshot)
