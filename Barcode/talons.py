#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
# import PyQt5.Qt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def print_talons():
    from reportlab.lib.units import mm
    cnv = canvas.Canvas("Talons.pdf", pagesize=A4)
    # move the origin up and to the left
    cnv.translate(mm, mm)
    # define a large font
    cnv.setFont("Helvetica", 14)
    # choose some colors
    cnv.setStrokeColorRGB(0.2, 0.5, 0.3)
    cnv.setFillColorRGB(1, 0, 1)
    # draw some lines
    cnv.line(0, 0, 0, 43 * mm)
    cnv.line(0, 0, 1 * mm, 0)
    # draw a rectangle
    cnv.rect(5 * mm, 5 * mm, 25.4 * mm, 38 * mm, fill=1)
    # make text go straight up
    cnv.rotate(90)
    # change color
    cnv.setFillColorRGB(0, 0, 0.77)
    # say hello (note after rotate the y coord needs to be negative!)
    cnv.drawString(10 * mm, -mm, "Hello World")
    cnv.showPage()
    cnv.save()


class Talons(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.setCheckable(True)
        btn.move(50, 50)
        btn.clicked[bool].connect(print_talons)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Печать талонов')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Talons()
    sys.exit(app.exec_())
