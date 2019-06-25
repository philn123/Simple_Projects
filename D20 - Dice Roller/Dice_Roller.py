import tkinter
import random
window = tkinter.Tk()
def Random_Number():
    My_Random = random.randint(1,20)

    dice_thrown.configure(text = "Rolled: " + str(My_Random))


MyTitle = tkinter.Label(window, text = "DnD Dice Roller", font = "Arial 16")
MyTitle.pack()

MyButton = tkinter.Button(window, text = "Roll", command = Random_Number)
MyButton.pack()

dice_thrown = tkinter.Label(window, font = "Arial 16")
dice_thrown.pack()


window.mainloop()