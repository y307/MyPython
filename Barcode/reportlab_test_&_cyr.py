#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://www.reportlab.com/documentation/


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

font_file = '/usr/share/fonts/truetype/msttcorefonts/arial.ttf'


def hello(c):
    from reportlab.lib.units import mm
    pdfmetrics.registerFont(TTFont('Arial', font_file))
    c.setFont('Arial', 10)
    c.translate(0, 294 * mm)
    c.drawString(10*mm, 0, 'Привет! № 123456')


c = canvas.Canvas("reportlab.pdf", pagesize=A4)
width, heigth = A4
hello(c)
c.showPage()
c.save()
