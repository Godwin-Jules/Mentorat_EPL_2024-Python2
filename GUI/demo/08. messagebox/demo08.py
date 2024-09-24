from tkinter import *   # type:ignore
from tkinter import messagebox

def show_message():
    messagebox.showinfo(title="INFORMATION", message="Hello, World!")
    # messagebox.showwarning(title="WARNING", message="Hello, World!")
    # messagebox.showerror(title="ERROR", message="Hello, World!")

    # if messagebox.askokcancel(title="QUESTION", message="Are you sure?"):
    #     print("You did it!")
    # else:
    #     show_message()

    # if messagebox.askretrycancel(title="QUESTION", message="Are you sure?"):
    #     print("You retried it!")
    # else:
    #     show_message()

    # if messagebox.askyesno(title="QUESTION", message="Are you sure?"):
    #     print("You accepted it!")
    # else:
    #     show_message()

    # answer = messagebox.askquestion(title="QUESTION", message="Do you like coding?")
    # if answer == "yes":
    #     print("You liked it!")
    # else:
    #     show_message()

    # answer =  messagebox.askyesnocancel(title="QUESTION", message="Do you want to code?", icon="warning")   # icon =("warning", "error", "info")
    # if answer:
    #     print("You liked it!")
    # elif answer == False:
    #     print("You didn't like it :(")
    # else:
    #     show_message()


frame = Tk()

button = Button(frame,
                text="Show Message",
                bg="#f7ffde",
                font=("Constantia", 15),
                command=show_message,
                padx=5,
                pady=2)
button.pack()

frame.mainloop()