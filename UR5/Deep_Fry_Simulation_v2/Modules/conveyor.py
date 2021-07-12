import sim
import globalvariables as g

#Initializes the basket by spawning it on a platform in the CoppeliaSim scene
def initBasket(arrIndex):
    errorCode, basketH = sim.simxGetObjectHandle(g.clientID, 'Basket' + arrIndex, sim.simx_opmode_blocking)
    sim.simxSetObjectPosition(g.clientID, basketH, -1, g.basket_spawn, sim.simx_opmode_oneshot)

