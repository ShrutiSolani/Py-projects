from tkinter import *
import random
print("Roll the Dice !!! ")
def dice():
    x = random.randint(1,6)
    print(x)

top = Tk()
top.geometry("200x100")
b = Button(top, text = "Roll again",command = dice)
b.pack(side = LEFT)
top.mainloop()
