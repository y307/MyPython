#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://www.reportlab.com/documentation/


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def hello(c):
    from reportlab.lib.units import mm
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    c.setFont('Arial', 10)
    c.translate(0, 294 * mm)
    c.drawString(10*mm, 0, 'Привет! № 123456')


c = canvas.Canvas("hello.pdf", pagesize=A4)
width, heigth = A4
hello(c)
c.showPage()
c.save()
