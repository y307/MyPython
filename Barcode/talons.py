#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
# import PyQt5.Qt


def print_talons():
    print('Event')


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
