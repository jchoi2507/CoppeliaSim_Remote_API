## basket.py is the module that commands which basket to perform what action. It was created to provide more readability
## to the basketfunctions.py module.

import basketfunctions as bf # Function definitions for basket module
import globalvariables as g # Global variables module

def moveBasket(arrIndex, targetPosition):
    if targetPosition == 0: #occupy position 1
        bf.moveBasketFunc(g.clientID, 1, arrIndex)
    elif targetPosition == 1: #occupy position 2
        bf.moveBasketFunc(g.clientID, 2, arrIndex)
    elif targetPosition == 2: #occupy position 3
        bf.moveBasketFunc(g.clientID, 3, arrIndex)
    elif targetPosition == 3: #occupy position 4
        bf.moveBasketFunc(g.clientID, 4, arrIndex)

def shakeBasket(arrIndex, targetPosition):
    if targetPosition == 0: #occupy position 1
        bf.shakeBasketFunc(g.clientID, 1, arrIndex)
    elif targetPosition == 1: #occupy position 2
        bf.shakeBasketFunc(g.clientID, 2, arrIndex)
    elif targetPosition == 2: #occupy position 3
        pass
    elif targetPosition == 3: #occupy position 4
        pass

def returnBasket(arrIndex, targetPosition):
    if targetPosition == 0: #occupy position 1
        bf.returnBasketFunc(g.clientID, 1, arrIndex)
    elif targetPosition == 1: #occupy position 2
        bf.returnBasketFunc(g.clientID, 2, arrIndex)
    elif targetPosition == 2: #occupy position 3
        pass
    elif targetPosition == 3: #occupy position 4
        pass
