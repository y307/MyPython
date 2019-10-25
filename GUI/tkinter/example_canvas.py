#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" При создании экземпляра Canvas необходимо указать его ширину и высоту.
    При размещении геометрических примитивов и других объектов указываются
    их координаты на холсте. Точкой отсчета является верхний левый угол (x=0, y=0)
"""

from tkinter import Canvas

root = Tk()
root.title("Печать талонов")
root.geometry("800x600")

c = Canvas(root, width=800, height=600, bg="white")
c.pack()

c.create_line(10, 10, 50, 60)

c.create_line(50, 160, 50, 80, fill="green", width=5, arrow=LAST, dash=(10, 2),
              activefill="lightgreen", arrowshape="10 20 10")

c.create_rectangle(80, 10, 120, 60)

c.create_rectangle(80, 80, 120, 160, fill='yellow', outline='green',
                   width=3, activedash=(5, 4))

# треугольник - вершина, левый угол, правый угол
c.create_polygon(220, 10, 160, 60, 280, 60)
# трапеция
c.create_polygon(190, 80, 250, 80, 280, 160, 160, 160,
                 fill='orange', outline='black')

# круг
c.create_oval(330, 10, 380, 60, width=2)
# овал
c.create_oval(300, 100, 410, 160, fill='grey70', outline='white')
# круг
c.create_oval(450, 10, 600, 160, fill='lightgrey', outline='white')
# сектор
c.create_arc(450, 10, 600, 160, start=0, extent=45, fill='red')
# сектор
c.create_arc(450, 10, 600, 160, start=180, extent=25, fill='orange')
# сегмент
c.create_arc(450, 10, 600, 160, start=240, extent=100, style=CHORD, fill='green')
# дуга
c.create_arc(450, 10, 600, 160, start=160, extent=-70, style=ARC, outline='darkblue', width=5)

c.create_text(200, 250, text="Hello World,\nPython\nand Tk", justify=CENTER, font="Verdana 14")
c.create_text(300, 300, text="About this", anchor=SE, fill="grey")

root.mainloop()
