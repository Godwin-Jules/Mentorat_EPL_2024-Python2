from tkinter import * # type:ignore

def display():
    if x.get():
        print("You agree")
    else:
        print("You do'nt agree :(")



frame = Tk()

x = BooleanVar() # IntVar is a special variable type for Tkinter
# x = IntVar() # IntVar is a special variable type for Tkinter
# x = StringVar() # StringVar is a special variable type for Tkinter

img = PhotoImage(file="favicon_modified_white.png")

ckeck_button = Checkbutton(frame,
                           text="I agree to the terms of conditions",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Arial", 20),
                           fg="whitesmoke",
                           bg="#2037aa",
                           activebackground="#2037aa",
                           activeforeground="whitesmoke",
                           padx=20,
                           pady=10,
                           image=img,
                           compound="left")
# Almost the same arguments as the label widget
# variable: a variable to store the value of the checkbutton
# onvalue: the value stored in the variable when the checkbutton is selected
# offvalue: the value stored in the variable when the checkbutton is deselected

ckeck_button.pack()

frame.mainloop()