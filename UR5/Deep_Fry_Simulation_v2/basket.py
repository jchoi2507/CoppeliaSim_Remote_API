import basketfunctions as bf # Function definitions for basket module
import globalvariables as g # Global variables module

def moveBasket(basketNum):
    if basketNum == 1:
        bf.b1MoveBasket(g.clientID)

    elif basketNum == 2:
        bf.b2MoveBasket(g.clientID)

def shakeBasket(basketNum):
    if basketNum == 1:
        bf.b1ShakeBasket(g.clientID)

    elif basketNum == 2:
        bf.b2ShakeBasket(g.clientID)

def returnBasket(basketNum):
    if basketNum == 1:
        bf.b1ReturnBasket(g.clientID)

    elif basketNum == 2:
        bf.b2ReturnBasket(g.clientID)
