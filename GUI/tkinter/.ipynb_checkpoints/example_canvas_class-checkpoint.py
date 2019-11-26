#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, Frame, BOTH, CHORD, ARC, CENTER, SE, LAST


class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)
        # canvas.create_line(15, 25, 200, 25)
        # canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.create_line(10, 10, 50, 60)

        canvas.create_line(50, 160, 50, 80, fill='green', width=5, arrow=LAST, dash=(10, 2), activefill='lightgreen', arrowshape="10 20 10")

        canvas.create_rectangle(80, 10, 120, 60)

        canvas.create_rectangle(80, 80, 120, 160, fill='yellow', outline='green', width=3, activedash=(5, 4))

        # треугольник - вершина, левый угол, правый угол
        canvas.create_polygon(220, 10, 160, 60, 280, 60)
        # трапеция
        canvas.create_polygon(190, 80, 250, 80, 280, 160, 160, 160, fill='orange', outline='black')

        # круг
        canvas.create_oval(330, 10, 380, 60, width=2)
        # овал
        canvas.create_oval(300, 100, 410, 160, fill='grey70', outline='black')
        # круг
        canvas.create_oval(450, 10, 600, 160, fill='lightgrey', outline='black')
        # сектор
        canvas.create_arc(450, 10, 600, 160, start=0, extent=45, fill='red')
        # сектор
        canvas.create_arc(450, 10, 600, 160, start=180, extent=25, fill='orange')
        # сегмент
        canvas.create_arc(450, 10, 600, 160, start=240, extent=100, style=CHORD, fill='green')
        # дуга
        canvas.create_arc(450, 10, 600, 160, start=160, extent=-70, style=ARC, outline='darkblue', width=5)

        canvas.create_text(200, 250, text="Hello World,\nPython\nand Tk", justify=CENTER, font="Verdana 14")
        canvas.create_text(300, 300, text="About this", anchor=SE, fill="grey")


def main():
    root = Tk()
    ex = MainWindow(root)
    root.geometry("800x600")
    root.mainloop()


if __name__ == '__main__':
    main()
