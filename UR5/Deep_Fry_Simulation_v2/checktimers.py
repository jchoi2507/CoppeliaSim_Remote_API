import time
from colorama import Fore
import threading

import globalvariables as g
import basketfunctions as bf
import UI as ui

def b1checkTimer(targetPosition, arrIndex):
    numOfShakes = 0
    while True:
        n = 0

        g.tableArr[n].endTimer()
        time.sleep(1)
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 60.0):
            bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
            numOfShakes = numOfShakes + 1
            g.tableArr[n].startTimer()

            if (numOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break

def b2checkTimer(targetPosition, arrIndex):
    numOfShakes = 0
    while True:
        n = 1

        g.tableArr[n].endTimer()
        time.sleep(1)
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 60.0):
            bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
            numOfShakes = numOfShakes + 1
            g.tableArr[n].startTimer()

            if (numOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break

def b3checkTimer(targetPosition, arrIndex):
    numOfShakes = 0
    while True:
        n = 2

        g.tableArr[n].endTimer()
        time.sleep(1)
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 60.0):
            bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
            numOfShakes = numOfShakes + 1
            g.tableArr[n].startTimer()

            if (numOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break

def b4checkTimer(targetPosition, arrIndex):
    numOfShakes = 0
    while True:
        n = 3

        g.tableArr[n].endTimer()
        time.sleep(1)
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 60.0):
            bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
            numOfShakes = numOfShakes + 1
            g.tableArr[n].startTimer()

            if (numOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break
