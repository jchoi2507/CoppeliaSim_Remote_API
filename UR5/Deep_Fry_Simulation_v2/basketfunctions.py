import time
import sim

import moveL as mL # move_L function module
import gripper as grip # Gripper functions module
import globalvariables as g # Global variables module

def b1MoveBasket(clientid):

    # Moving to initial position
    mL.move_L(clientid, g.target, g.b1_initial_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket1, g.connector, True, sim.simx_opmode_blocking)

    # Closing gripper
    grip.gripper_function(clientid, 1, g.j1, g.j2, g.p1, g.p2)
    time.sleep(0.9)
    grip.pause_gripper(clientid, g.j1, g.j2)
    time.sleep(1)

    # Moving object to second table
    mL.move_L(clientid, g.target, g.b1_int_pos, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_2, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_3, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_4, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_5, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_final_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket1, -1, True, sim.simx_opmode_blocking)
    grip.gripper_function(clientid, 0, g.j1, g.j2, g.p1, g.p2)

    # Moving robotic arm back to first table, ready to move basket #2
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_5, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_4, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_3, 2)
    time.sleep(1)

def b2MoveBasket(clientid):
    # Moving to initial position
    mL.move_L(clientid, g.target, g.b2_initial_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket2, g.connector, True, sim.simx_opmode_blocking)
    time.sleep(1)

    # Closing gripper
    grip.gripper_function(clientid, 1, g.j1, g.j2, g.p1, g.p2)
    time.sleep(0.9)
    grip.pause_gripper(clientid, g.j1, g.j2)
    time.sleep(2)

    # Moving object to second table
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
    sim.simxSetObjectParent(clientid, g.basket2, -1, True, sim.simx_opmode_blocking)
    grip.gripper_function(clientid, 0, g.j1, g.j2, g.p1, g.p2)

    # Moving robotic arm back to original position
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b2_int_pos_5, 2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b2_int_pos_4, 2)
    time.sleep(1)

def b1ReturnBasket(clientid):
    b1_return_pos = [-1.725, 0.4, 0.552, 0, 0, 0]

    mL.move_L(clientid, g.target, g.b1_final_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket1, g.connector, True, sim.simx_opmode_blocking)
    time.sleep(1)
    grip.gripper_function(clientid, 1, g.j1, g.j2, g.p1, g.p2)
    time.sleep(0.6)
    grip.pause_gripper(clientid, g.j1, g.j2)
    time.sleep(1)
    mL.move_L(clientid, g.target, g.b1_int_pos_5, 2)
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
    sim.simxSetObjectParent(clientid, g.basket1, -1, True, sim.simx_opmode_blocking)
    time.sleep(1)
    grip.gripper_function(clientid, 0, g.j1, g.j2, g.p1, g.p2)
    time.sleep(2)
    mL.move_L(clientid, g.target, g.b2_int_pos_3, 2)
    time.sleep(2)

def b2ReturnBasket(clientid):
    b2_return_pos = [-1.725, 0.6, 0.552, 0, 0, 0]

    mL.move_L(clientid, g.target, g.b2_final_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket2, g.connector, True, sim.simx_opmode_blocking)
    time.sleep(1.5)
    grip.gripper_function(clientid, 1, g.j1, g.j2, g.p1, g.p2)
    time.sleep(0.6)
    grip.pause_gripper(clientid, g.j1, g.j2)
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
    sim.simxSetObjectParent(clientid, g.basket2, -1, True, sim.simx_opmode_blocking)
    time.sleep(1)
    grip.gripper_function(clientid, 0, g.j1, g.j2, g.p1, g.p2)
    time.sleep(1)

def b1ShakeBasket(clientid):
    b1_back_pos = [-1.6, 0.81, 0.52, 0, 0, 0]

    mL.move_L(clientid, g.target, g.b1_final_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket1, g.connector, True, sim.simx_opmode_blocking)
    grip.gripper_function(clientid, 1, g.j1, g.j2, g.p1, g.p2)
    time.sleep(0.6)
    grip.pause_gripper(clientid, g.j1, g.j2)
    time.sleep(1)

    for i in range(6):
        mL.move_L(clientid, g.target, b1_back_pos, 2)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b1_final_pos, 2)

def b2ShakeBasket(clientid):
    b2_back_pos = [-1.6, 0.97, 0.52, 0, 0, 0]

    mL.move_L(clientid, g.target, g.b2_final_pos, 2)
    time.sleep(3)
    sim.simxSetObjectParent(clientid, g.basket2, g.connector, True, sim.simx_opmode_blocking)
    grip.gripper_function(clientid, 1, g.j1, g.j2, g.p1, g.p2)
    time.sleep(0.6)
    grip.pause_gripper(clientid, g.j1, g.j2)
    time.sleep(1)

    for i in range(6):
        mL.move_L(clientid, g.target, b2_back_pos, 2)
        time.sleep(0.5)
        mL.move_L(clientid, g.target, g.b2_final_pos, 2)
