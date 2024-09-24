from tkinter import *   # type:ignore

def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())
    entry_box.delete(0, END)

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

def submit():
    skills = []
    for index in listbox.curselection():
        skills.insert(index, listbox.get(index))

    for skill in skills:
        print(skill)



frame = Tk()

listbox = Listbox(frame,
                  bg="#f7ffde",
                  font=("Constantia", 15),
                  width=15,
                  selectmode=MULTIPLE)
# Almost the same arguments of le label widget
listbox.pack()

listbox.insert(1, "Python")
listbox.insert(2, "C")
listbox.insert(3, "Java")
listbox.insert(4, "PHP")
listbox.insert(5, "C++")
listbox.insert(6, "JavaScript")

listbox.config(height=listbox.size())   # Adjust the height of the listbox dynamically

entry_box = Entry(frame,
              bg="#f7ffde",
              font=("Constantia", 15),
              width=20,
              )
entry_box.pack()

add_button = Button(frame,
                    text="Add",
                    bg="#f7ffde",
                    font=("Constantia", 10),
                    command=add,
                    padx=5,
                    pady=2)
add_button.pack()

delete_button = Button(frame,
                       text="Delete",
                       bg="#f7ffde",
                       font=("Constantia", 10),
                       command=delete,
                       padx=5,
                       pady=2)
delete_button.pack()

submit_button = Button(frame,
                       text="Submit",
                       bg="#f7ffde",
                       font=("Constantia", 15),
                       command=submit,
                       padx=15,
                       pady=2)
submit_button.pack()




frame.mainloop()