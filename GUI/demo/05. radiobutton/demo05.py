from tkinter import *   # type:ignore

foods = ["pizza", "humburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered humburger")
    elif x.get() == 2:
        print("You ordered hotdog")
    else:
        print("You ordered nothing")

frame = Tk()

x = IntVar()
for index in range(len(foods)):

    radio_button = Radiobutton(frame, 
                               text=foods[index], # add text to radio buttons
                               variable=x, # groups radioubttons together if they share the same variable
                               value=index, # assigns a value to each different radio button
                               padx=25,
                               pady=10,
                               font=("Comic Sans MS", 20),
                               indicatoron=False, # eliminate circle indicators
                               width=40, # width of the radio button
                               command=order)
    radio_button.pack(anchor=W) # aligns the radio buttons to the left

frame.mainloop()