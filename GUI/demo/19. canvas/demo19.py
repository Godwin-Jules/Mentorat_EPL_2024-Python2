from tkinter import *       #type:ignore

# canvas is a widget that allows you to draw shapes, images, and other widgets on it. It is a very powerful widget that can be used to create a wide range of applications. It's almost like Turtle

root = Tk()

canvas = Canvas(root, width=500, height=500)
"""canvas.create_line(0, 0, 500, 500, fill="red", width=5) # create a line from (0,0) to (500,500) with a width of 5 and color red
# fill : specify the color of  your shape"""

# canvas.create_line(0, 500, 500, 0, fill="blue", width=5)
# canvas.create_rectangle(50, 50,400, 300, fill="green") # create a rectangle from (50,50) to (200,200) with a color of green

"""points = [10, 10, 200, 20, 300, 400, 150, 120]
canvas.create_polygon(points, fill="gray", outline="#2037aa", width=5) # create a polygon with 3 points
# outline : the color of the shape's border
# width : the width of the shape's border"""



"""canvas.create_arc(0, 0, 500, 500, start=0, extent=150, fill="yellow", style=CHORD) # create an arc from (0,0) to (500,500) with a start angle of 0 and an extent of 180
# start : the start angle of the arc
# extent : the extent of the arc in degrees
# style : the style of the arc (PIESLICE, CHORD, ARC)"""

# canvas.create_oval(50, 50, 400, 300, fill="yellow") # create an oval from (50,50) to (400,300) with a color of yellow

# Creating a poke ball
canvas.create_arc(0, 0, 500, 500, extent=180, fill="red", width=5)
canvas.create_arc(0, 0, 500, 500, start=180, extent=180, fill="white", width=5)
canvas.create_oval(180, 180, 320, 320, fill="white", width=10)



canvas.pack()

root.mainloop()