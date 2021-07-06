from tkinter import * # Python UI library

countArr = ["", "0", "1", "2"]
counter = 0

root = Tk()

boneChickenPicture = PhotoImage(file='boneResizedWithText.png')
bonelessChickenPicture = PhotoImage(file='bonelessResizedWithText.png')

button1 = Button(root, padx=10, pady=10, image=boneChickenPicture,
                 command=lambda: cc.boneChicken(countArr[counter]))
button2 = Button(root, padx=10, pady=10, image=bonelessChickenPicture,
                 command=lambda: cc.bonelessChicken(countArr[counter]))

button1.pack()
button2.pack()

root.mainloop()
counter = counter + 1
