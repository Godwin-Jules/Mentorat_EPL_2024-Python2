from tkinter import *   # type:ignore
from tkinter import colorchooser

def getColor():
    # frame.config(bg=colorchooser.askcolor()[1])
    color = colorchooser.askcolor()
    color_hex:str = color[1]    # type:ignore
    frame.config(bg=color_hex)


frame = Tk()
frame.geometry("420x420")

button = Button(frame, text="Select Color", command=getColor)
button.pack()

frame.mainloop()