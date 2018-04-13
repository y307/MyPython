#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://python-3.ru/page/dialogs-in-pyqt5

import sys
from PyQt5.QtWidgets import (QMainWindow, QLineEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class VideoTs(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Download')
        self.setGeometry(300, 300, 350, 300)

        line_edit = QLineEdit(self)
        line_edit.move(0, 0)
        line_edit.size(10,100)

        self.show()

    '''
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        f = open(fname[0], 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

        f.close()
    '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoTs()
    sys.exit(app.exec_())
