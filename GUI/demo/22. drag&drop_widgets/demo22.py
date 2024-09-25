from tkinter import *   # type:ignore

def drag_start(event):
    widget = event.widget   # get the widget that we are dealing with
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

root = Tk()

label_one = Label(root, bg="red", width=10, height=5)
label_one.place(x=0, y=0)

label_two = Label(root, bg="blue", width=10, height=5)
label_two.place(x=100, y=100)

# How to bind a widgetlabel.bind(event, function)
label_one.bind("<Button-1>", drag_start)    # The left mouse click
label_one.bind("<B1-Motion>", drag_motion)    # Holding left mouse key and motion
label_two.bind("<Button-1>", drag_start)
label_two.bind("<B1-Motion>", drag_motion)

root.mainloop()