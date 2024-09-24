from tkinter import *   # type:ignore

def submit():
    input = text.get("1.0", END)
    print(input)


frame = Tk()

text = Text(frame, 
            bg="light yellow",
            font=("Ink Free", 25),
            height=10, 
            width=50,
            padx=10,
            pady=10,
            fg="purple")
text.pack()

button = Button(frame,
                text="Submit",
                command=submit)
button.pack()

frame.mainloop()