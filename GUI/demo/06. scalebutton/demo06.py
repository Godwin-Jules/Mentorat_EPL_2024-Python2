from tkinter import *   # type:ignore

frame = Tk()

scale = Scale(frame, 
              from_=0, 
              to=1000, 
              orient=VERTICAL,
              length=500,
              tickinterval=10,
              resolution=5,
              label="Scale",
              troughcolor="#2037aa",
              sliderlength=20,
              showvalue=False,)
scale.set(scale['to']+(scale['from']-scale['to'])/2)
scale.pack()

button = Button(frame, text="Get scale value", command=lambda: print(scale.get()))
button.pack()


frame.mainloop()