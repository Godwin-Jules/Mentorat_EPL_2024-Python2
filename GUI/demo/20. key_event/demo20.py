from tkinter import *   # type:ignore

def perform_action(event):
    print("You pressed:", event.keysym)    # keysym is a property that returns the key that was pressed
    key_label.config(text=event.keysym)



root = Tk()

# How it works root.bind(event, function)   event = "<key>"
# root.bind("<Key>", perform_action) will take account of any key
# root.bind("<Return>", perform_action)
root.bind("<Key>", perform_action)

key_label = Label(root, text="Press any key", font=("Helvetica", 20), width=30, height=10)
key_label.pack()
root.mainloop()