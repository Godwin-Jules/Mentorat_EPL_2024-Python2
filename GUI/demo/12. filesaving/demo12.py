from tkinter import *   # type:ignore
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")],
                                    initialdir=r"D:\PROJECTS\ORIGINALS\Mentorat_EPL_2024-Python2\GUI\demo\12. filesaving")
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)   # type:ignore
    file.close()    #type:ignore


root = Tk()

text = Text(root)
text.pack()
button = Button(text="Save", command=saveFile)
button.pack()

root.mainloop()