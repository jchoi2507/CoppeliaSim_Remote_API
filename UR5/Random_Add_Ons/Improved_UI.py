from tkinter import * # Python UI library

def incCounter():
    global counter
    counter = counter + 1

countArr = ["", "0", "1", "2"]
counter = 0

root = Tk()

boneChickenPicture = PhotoImage(file='boneResizedWithText.png')
bonelessChickenPicture = PhotoImage(file='bonelessResizedWithText.png')

button1 = Button(root, padx=10, pady=10, image=boneChickenPicture,
                 command=lambda: [cc.boneChicken(countArr[counter], counter), incCounter()]) #Incorporating lambda is necessary in order to execute two functions INSIDE mainloop()
button2 = Button(root, padx=10, pady=10, image=bonelessChickenPicture,
                 command=lambda: [cc.bonelessChicken(countArr[counter], counter), incCounter()])

button1.pack()
button2.pack()

root.mainloop()
