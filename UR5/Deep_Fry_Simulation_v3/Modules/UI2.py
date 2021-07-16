import globalvariables as g

def t1Display(b1shake_left):
    typeOfChicken = g.tableArr[0].type
    if (b1shake_left > 1000): #Accounting for the 'time glitch' where displayed time >>>> 1000
        return "Basket 1: is empty."

    elif (g.tableArr[0].empty == False):
        t1ShakesLeft = 3 - g.t1NumOfShakes
        if (g.t1NumOfShakes != 3):
            return "Basket 1: " + "[" + typeOfChicken + "] " + str(b1shake_left) + " seconds left to next shake. " + str(t1ShakesLeft) + " shake(s) left."
        elif (g.t1NumOfShakes == 3):
            if (b1shake_left <= 0):
                return "Basket 1: " + "[" + typeOfChicken + "] " + "completed."
            else:
                return "Basket 1: " + "[" + typeOfChicken + "] " + str(b1shake_left) + " seconds until completion."

    else:
        return "Basket 1: is empty."

def t2Display(b2shake_left):
    typeOfChicken = g.tableArr[1].type
    if (b2shake_left > 1000):
        return "Basket 2: is empty."

    elif (g.tableArr[1].empty == False):
        t2ShakesLeft = 3 - g.t2NumOfShakes
        if (g.t2NumOfShakes != 3):
            return "Basket 2: " + "[" + typeOfChicken + "] " + str(b2shake_left) + " seconds left to next shake. " + str(t2ShakesLeft) + " shake(s) left."
        elif (g.t2NumOfShakes == 3):
            if (b2shake_left <= 0):
                return "Basket 2: " + "[" + typeOfChicken + "] " + "completed."
            else:
                return "Basket 2: " + "[" + typeOfChicken + "] " + str(b2shake_left) + " seconds until completion."

    else:
        return "Basket 2: is empty."

def t3Display(b3shake_left):
    typeOfChicken = g.tableArr[2].type
    if (b3shake_left > 1000):
        return "Basket 3: is empty."

    elif (g.tableArr[2].empty == False):
        t3ShakesLeft = 3 - g.t3NumOfShakes
        if (g.t3NumOfShakes != 3):
            return "Basket 3: " + "[" + typeOfChicken + "] " + str(b3shake_left) + " seconds left to next shake. " + str(t3ShakesLeft) + " shake(s) left."
        elif (g.t3NumOfShakes == 3):
            if (b3shake_left <= 0):
                return "Basket 3: " + "[" + typeOfChicken + "]" + " completed."
            else:
                return "Basket 3: " + "[" + typeOfChicken + "] " + str(b3shake_left) + " seconds until completion."

    else:
        return "Basket 3: is empty."

def t4Display(b4shake_left):
    typeOfChicken = g.tableArr[3].type
    if (b4shake_left > 1000):
        return "Basket 4: is empty."

    elif (g.tableArr[3].empty == False):
        t4ShakesLeft = 3 - g.t4NumOfShakes
        if (g.t4NumOfShakes != 3):
            return "Basket 4: " + "[" + typeOfChicken + "] " + str(b4shake_left) + " seconds left to next shake. " + str(t4ShakesLeft) + " shake(s) left."
        elif (g.t4NumOfShakes == 3):
            if (b4shake_left <= 0):
                return "Basket 4: " + "[" + typeOfChicken + "] " + "completed."
            else:
                return "Basket 4: " + "[" + typeOfChicken + "] " + str(b4shake_left) + " seconds until completion."

    else:
        return "Basket 4: is empty."
