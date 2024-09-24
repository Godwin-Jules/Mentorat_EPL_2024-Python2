from tkinter import *   # type:ignore
from tkinter import messagebox
from PIL import Image, ImageTk


def openFile():
    print("Open file")

def saveFile():
    print("Save file")

def quit():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
    else:
        return

def copy():
    print("Copy")

def cut():
    print("Cut")

def paste():
    print("Paste")

def resize_image(image_path:str, width:int, height:int):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)

    return ImageTk.PhotoImage(img)


root = Tk()


open_image = resize_image("open.png", 15, 15)
save_image = resize_image("save.png", 15, 15)
exit_image = resize_image("exit.png", 15, 15)
copy_image = resize_image("copy.png", 15, 15)
cut_image = resize_image("cut.png", 15, 15)
paste_image = resize_image("paste.png", 15, 15)









menubar = Menu(root)    # create a menu bar
root.config(menu=menubar)   # attach the menu bar to the root window
file_menu = Menu(menubar, tearoff=False)   # create a menu item
menubar.add_cascade(label="File", menu=file_menu)  # add the menu item to the menu bar
file_menu.add_command(label="Open", command=openFile, image=open_image, compound="left")
file_menu.add_command(label="Save", command=saveFile, image=save_image, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_image, compound="left")

edit_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy, image=copy_image, compound="left")
edit_menu.add_command(label="Cut", command=cut, image=cut_image, compound="left")
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste, image=paste_image, compound="left")

root.mainloop()