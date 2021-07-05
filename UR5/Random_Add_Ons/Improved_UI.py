from tkinter import *
root = Tk()
root.geometry("700x700")
root.title("Robert Chicken Menu")

def command1():
    print("Preparing your boned chicken!")

def command2():
    print("Preparing your boneless chicken!")

#Adding pictures as the buttons in the menu
boneChickenPicture = PhotoImage(file = 'boneResizedWithText.png')
bonelessChickenPicture = PhotoImage(file = 'bonelessResizedWithText.png')

button1 = Button(root, text = "Bone Chicken", padx = 10, pady = 10, image = boneChickenPicture,
                 command = lambda: command1())
button2 = Button(root, text = "Boneless Chicken", padx = 10, pady = 10, image = bonelessChickenPicture,
                 command = lambda: command2())

button1.pack()
button2.pack()

root.mainloop()
