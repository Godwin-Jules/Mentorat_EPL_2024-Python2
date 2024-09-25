from tkinter import *   # type:ignore
from tkinter import ttk     # useful to create tabs (notebook)


root = Tk()

notebook = ttk.Notebook(root)   # create a notebook: widget that manages a collection of windows and displays one at a time

tab_one = Frame(notebook)   # create a frame for the first tab
tab_two = Frame(notebook)   # create a frame for the second tab

notebook.add(tab_one, text='Tab 1')   # add the first tab to the notebook
notebook.add(tab_two, text='Tab 2')   # add the second tab to the notebook

notebook.pack(expand=True, fill="both")   # pack the notebook
# expand: expand the widget to fill any space not otherwise used in widget's parent
# fill: fill the widget's parent in the direction of the parent's packing (on x and y axis)

Label(tab_one, text="Hi everyone - Tab One", width=50, height=25).pack()
Label(tab_two, text="Hi everyone - Tab Two", width=50, height=25).pack()


root.mainloop()