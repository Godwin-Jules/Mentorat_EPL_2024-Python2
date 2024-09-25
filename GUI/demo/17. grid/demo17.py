from tkinter import *   # type:ignore

root = Tk()

# grid: it is used to place the widgets in a 2D table-like structure. It gives you more control over the layout of your widgets.
title_label = Label(root, text="Registration Form", font=("Georgia", 25, "bold"), fg="#2037aa", width=25).grid(row=0,column=0, columnspan=2)

first_name_label = Label(root, text="First Name: ", font=("Arial", 15), fg="black").grid(row=1,column=0)
first_name_entry = Entry(root, width=50).grid(row=1,column=1)

last_name_label = Label(root, text="Last Name: ", font=("Arial", 15), fg="black").grid(row=2,column=0)
last_name_entry = Entry(root, width=50).grid(row=2,column=1)

email_name_label = Label(root, text="Email Address: ", font=("Arial", 15), fg="black").grid(row=3,column=0)
email_name_entry = Entry(root, width=50).grid(row=3,column=1)

submit_button = Button(root, text="Submit", font=("Arial", 15, "bold"), fg="green").grid(row=4,column=0, columnspan=2)
# columnspan: it is used to specify the number of columns a widget should span (cover/be extended).


root.mainloop()