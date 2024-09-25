from tkinter import *   # type:ignore

def perform_action(event):
    print("Mouse coordinates: ", event.x, ",", event.y)



root = Tk()

# root.bind("<Key>", perform_action)
# root.bind("<Button-1>", perform_action) # left mouse click
# root.bind("<Button-2>", perform_action) # scroll wheel click
# root.bind("<Button-3>", perform_action) # right mouse click
# root.bind("<ButtonRelease>", perform_action) # as soon as a mouse button click is released
# root.bind("<Enter>", perform_action) # When the mouse enter the window / the interface zone / hover the GUI
# root.bind("<Leave>", perform_action) # Opposite of Enter, when the mouse leaves the window
root.bind("<Motion>", perform_action) # Where the mouse moved

key_label = Label(root, text="Use you mouse", font=("Helvetica", 20), width=30, height=10)
key_label.pack()
root.mainloop()