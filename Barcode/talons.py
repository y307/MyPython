#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
# import PyQt5.Qt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# from Barcode.cyrillic4pdf import *
import Barcode.cyrillic4pdf as cyr


def print_talons():
    from reportlab.lib.units import mm
    cnv = canvas.Canvas("Talons.pdf", pagesize=A4)
    # move the origin up and to the left
    cnv.translate(0, 285 * mm)
    # define a large font
    font_name = cyr.set_cyr_font()
    cnv.setFont(font_name, 10)
    cnv.drawString(0, 0, 'Серия "Д" № 123456')
    # choose some colors
    # draw some lines
    # cnv.line(0, 0, 0, 43 * mm)
    # cnv.line(0, 0, 1 * mm, 0)
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
