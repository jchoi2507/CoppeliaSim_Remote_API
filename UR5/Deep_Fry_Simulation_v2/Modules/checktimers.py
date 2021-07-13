# The functions in checktimers.py are meant to be called in threads, to constantly check if a basket needs to be shaken.

import time
import globalvariables as g
import basketfunctions as bf

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
def b1checkTimer(targetPosition, arrIndex):
    while True:
        n = 0

        g.tableArr[n].endTimer()
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 80.0):
            if (g.t1NumOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break

            else:
                bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
                g.tableArr[n].startTimer()
                g.t1NumOfShakes = g.t1NumOfShakes + 1

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
def b2checkTimer(targetPosition, arrIndex):
    while True:
        n = 1

        g.tableArr[n].endTimer()
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 80.0):
            if (g.t2NumOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break
            
            else:
                bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
                g.tableArr[n].startTimer()
                g.t2NumOfShakes = g.t2NumOfShakes + 1

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
def b3checkTimer(targetPosition, arrIndex):
    while True:
        n = 2

        g.tableArr[n].endTimer()
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 80.0):
            if (g.t3NumOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break

            else:
                bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
                g.tableArr[n].startTimer()
                g.t3NumOfShakes = g.t3NumOfShakes + 1

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
def b4checkTimer(targetPosition, arrIndex):
    while True:
        n = 3

        g.tableArr[n].endTimer()
        elapsedTime = g.tableArr[n].endTime - g.tableArr[n].startTime

        if (elapsedTime >= 80.0):
            if (g.t4NumOfShakes == 3):
                bf.returnBasketFunc(g.clientID, targetPosition, arrIndex)
                break

            else:
                bf.shakeBasketFunc(g.clientID, targetPosition, arrIndex)
                g.tableArr[n].startTimer()
                g.t4NumOfShakes = g.t4NumOfShakes + 1

#Accounts for multiple baskets in the deep fryer system by delaying moving a basket until shaking is performed
def delayIfNecessary():
    t1_left = 80.0 - (g.t1.endTime - g.t1.startTime)
    t2_left = 80.0 - (g.t2.endTime - g.t2.startTime)
    t3_left = 80.0 - (g.t3.endTime - g.t3.startTime)
    t4_left = 80.0 - (g.t4.endTime - g.t4.startTime)

    if (t1_left < 20.0): #The robotic arm won't move the basket until the previous basket is done shaking
        time.sleep(t1_left + 12.0)
    
    elif (t2_left < 20.0):
        time.sleep(t2_left + 12.0)
    
    elif (t3_left < 20.0):
        time.sleep(t3_left + 12.0)

