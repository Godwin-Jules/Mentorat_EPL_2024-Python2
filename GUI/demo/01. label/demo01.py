"""Graphical User Interface (GUI)"""
from tkinter import *   # type:ignore Importing the tkinter module

window = Tk()   # Instanciation of a window
# window.geometry("420x420")      # Resizing the window
# window.geometry("480x480+500+200")  # Another way to resize the windows
window.title("My first GUI")    # Title of the window
icon = PhotoImage(file="favicon_modified_white.png")    # Creating an icon for the window
window.iconphoto(True, icon)    # Setting an icon of the window
window.config(background="#2037aa")    # Setting the background color of the window
# the config() method gives you access to the window's attributes and its control

# Creating widgets
label = Label(window, 
              text="Hi everyone", 
              font=("Arial", 40, "bold"), 
              fg="#2037aa", 
              bg="whitesmoke", 
              relief=RIDGE, 
              bd=10, 
              padx=20, 
              pady=20, 
              image=icon, 
              compound="bottom")   # Creating a label
# text: for the text to be displayed
# font: for the font of the text (font-family, font-size, font-weight)
# fg: for the color of the text
# bg: for the background color of the label
# relief: for the border of the label (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
# bd: for the border width of the label
# padx: for the padding in the x-axis
# pady: for the padding in the y-axis
# image: for the image to be displayed in the label
# compound: for the position of the image in the label (top, bottom, left, right)
label.pack()    # Displaying the label in the window
# label.place(x=0, y=0)   # Another way to place or display a label in the widnow

window.mainloop()  # Display the window