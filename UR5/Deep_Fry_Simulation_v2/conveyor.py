import sim

import globalvariables as g

def initBasket(arrIndex):

    relativeToParent = [0.18, 0, 0.058]
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)
    errorCode, cuboidH = sim.simxGetObjectHandle(g.clientID, 'Cuboid' + arrIndex, sim.simx_opmode_blocking)

    sim.simxSetObjectParent(g.clientID, basketH, cuboidH, False, sim.simx_opmode_blocking)  # play around w/ True and False to see which one works best
    sim.simxSetObjectPosition(g.clientID, basketH, sim.sim_handle_parent, relativeToParent, sim.simx_opmode_oneshot)
