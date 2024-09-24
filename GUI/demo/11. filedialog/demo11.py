from tkinter import *   # type:ignore
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir=r"D:\PROJECTS\ORIGINALS\Mentorat_EPL_2024-Python2",
                                          title="Open file",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")) )
    try:
        file = open(filepath, 'r')
        print(file.read())
        file.close()
    except PermissionError:
        print("Do not have permission to read that file")
    except Exception:
        print("Unable to open that file")



root = Tk()

button = Button(text="Open", command=openFile)
button.pack()

root.mainloop()