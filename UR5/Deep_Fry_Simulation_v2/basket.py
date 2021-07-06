## basket.py is the module that commands which basket to perform what action. It was created to provide more readability
## to the basketfunctions.py module.

import basketfunctions as bf # Function definitions for basket module
import globalvariables as g # Global variables module

def moveBasket(targetPosition, arrIndex):
    if targetPosition == 1:
        bf.moveBasketFunc(g.clientID, 1, arrIndex)
    elif targetPosition == 2:
        bf.moveBasketFunc(g.clientID, 2, arrIndex)
    elif targetPosition == 3:
        pass
    elif targetPosition == 4:
        pass

def shakeBasket(targetPosition, arrIndex):
    if targetPosition == 1:
        bf.shakeBasketFunc(g.clientID, 1, arrIndex)
    elif targetPosition == 2:
        bf.shakeBasketFunc(g.clientID, 2, arrIndex)
    elif targetPosition == 3:
        pass
    elif targetPosition == 4:
        pass

def returnBasket(targetPosition, arrIndex):
    if targetPosition == 1:
        bf.returnBasketFunc(g.clientID, 1, arrIndex)
    elif targetPosition == 2:
        bf.returnBasketFunc(g.clientID, 2, arrIndex)
    elif targetPosition == 3:
        pass
    elif targetPosition == 4:
        pass
