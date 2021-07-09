import time
import globalvariables as g
import basketfunctions as bf #'Body' of the chicken-cooking functions module

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
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

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
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

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
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

#To be called in a thread, this function continuously checks if the basket is ready to be shaken (up to 3 times)
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

#Accounts for multiple baskets in the deep fryer system (TOTAL SHAKING TIME: ~11 SECONDS)
def delayIfNecessary():
    t1_left = 60.0 - (g.t1.endTime - g.t1.startTime)
    t2_left = 60.0 - (g.t2.endTime - g.t2.startTime)
    t3_left = 60.0 - (g.t3.endTime - g.t3.startTime)
    t4_left = 60.0 - (g.t4.endTime - g.t4.startTime)

    if (t1_left < 20.0): #The robotic arm won't move the basket until the previous basket is done shaking
        time.sleep(t1_left + 12.0)
    
    elif (t2_left < 20.0):
        time.sleep(t2_left + 12.0)
    
    elif (t3_left < 20.0):
        time.sleep(t3_left + 12.0)

