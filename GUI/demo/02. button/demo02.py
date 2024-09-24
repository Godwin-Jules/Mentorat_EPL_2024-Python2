from tkinter import *    #type:ignore

window = Tk()
window.title("Button with tkinter")

count = 0
def click():
    global count
    count += 1
    print(count)
img = PhotoImage(file="favicon_modified_white.png")
button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="white",
                bg="#2037aa",
                activebackground="black",
                activeforeground="#2037aa",
                state=ACTIVE,
                image=img,
                compound="bottom")    # Creating a button
# text: the button text to be displayed
# Almost the same arguments as the Label widget
# activebackground: the background color when the button is clicked
# activeforeground: the text color when the button is clicked
# state: DISABLED, NORMAL, ACTIVE to set the button clickable or not

button.pack()


window.mainloop()