
from tkinter import *


root = Tk()

canvas_width = 150
canvas_height = 50
cnv = Canvas(root, width=canvas_width, height=canvas_height)
cnv.pack()

y = int(canvas_height / 8)
cnv.create_line(0, y, canvas_width, y, fill="#476042")

y = int(canvas_height / 4)
x=20
cnv.create_rectangle(x,y,x+10,y+30,fill='black')


mainloop()