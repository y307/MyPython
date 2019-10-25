#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas

root = Tk()

canvas_width = 150
canvas_height = 50
cnv = Canvas(root, width=canvas_width, height=canvas_height)
cnv.pack()

y = int(canvas_height / 8)
cnv.create_line(0, y, canvas_width, y, fill="#476042")

y = int(canvas_height / 4)
x1=20
x2=23
cnv.create_rectangle(x1, y, x2, y+30, fill='black')
x1=x2
x2+=3
cnv.create_rectangle(x1, y, x2, y+30, fill='white')

mainloop()
