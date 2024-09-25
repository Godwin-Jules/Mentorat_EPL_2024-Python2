from tkinter import *   # type:ignore

def create_window():
    window = Tk()           # Toplevel() is used to create a new window "on top" of other windows. When you destroy the main window, all other toplevel windows are destroyed as well. So it depends on the main window.
                            # Tk() is used to create a new window. When you destroy the main window, all other windows are not destroyed. So it is independent of the main window. Useful when your application deals with login interface and main interface for example. So the main interface must be totally independent of the login one
    window.title("New Window")
    window.geometry("300x200")
    root.destroy()

root = Tk()

Button(root,text="Create Window",font=("Arial", 12),width=15,command=create_window).pack()


root.mainloop()