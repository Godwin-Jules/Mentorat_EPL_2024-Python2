from tkinter import *   # type:ignore

root = Tk()

frame = Frame(root, bg="pink")
# frame.place(relx=0.7, rely=0.2, anchor=CENTER)
# frame.place(x=0, y=0)

Button(frame,text="Button 1",font=("Arial", 12),width=7).pack(side=TOP)
Button(frame,text="Button 2",font=("Arial", 12),width=7).pack(side=LEFT)
Button(frame,text="Button 3",font=("Arial", 12),width=7).pack(side=RIGHT)
Button(frame,text="Button 4",font=("Arial", 12),width=7).pack(side=BOTTOM)
Button(frame,text="Button 5",font=("Arial", 12),width=7).pack(side=BOTTOM)

root.mainloop()