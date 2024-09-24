from tkinter import *   # type:ignore

frame =Tk()

def submit():
    username = entry.get()
    print("Hello",username)
    entry.config(state=DISABLED)    # disable the entry widget

def delete():
    entry.delete(0, END)    # delete from index 0 to the end

def backspace():
    entry.delete(len(entry.get())-1, END)    # delete the last character

entry = Entry(frame,
              font=("Arial", 50),
              bg="whitesmoke",
              fg="#2037aa",
              show="*")
# width: the width of the entry widget
# borderwidth: the width of the border around the entry widget
# Almost the same arguments as the label widget
# entry.insert(0, "Enter your name")  # insert something into the entry widget
entry.pack(side=LEFT)
# side: LEFT, RIGHT, TOP, BOTTOM to set the position of the widget
# So you can add any arguents you want to customize your widget


delete_button = Button(frame, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

submit_button = Button(frame, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

backspace_button = Button(frame, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)


frame.mainloop()