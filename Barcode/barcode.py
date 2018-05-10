#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# barcode EAN-13

from tkinter import *
# import Image, ImageDraw
from PIL import Image, ImageDraw
import os

#####################################################################


def check_digit(acode):
    pos = 11
    factor = 3
    summ = 0

    while pos >= 0:
        # четные позиции умножаются на 3
        summ += int(acode[pos]) * factor
        # смена множителя на 1 или 3 при каждой итерации
        factor = 4 - factor
        # позиция следующей цифры
        pos -= 1

    res = summ % 10
    if res != 0:
        res = 10 - res

    return res


######################################################################


def coding(acode):
    list_A = ('0001101', '0011001', '0010011', '0111101', '0100011',
              '0110001', '0101111', '0111011', '0110111', '0001011')
    list_B = ('0100111', '0110011', '0011011', '0100001', '0011101',
              '0111001', '0000101', '0010001', '0001001', '0010111')
    list_C = ('1110010', '1100110', '1101100', '1000010', '1011100',
              '1001110', '1010000', '1000100', '1001000', '1110100')
    list_AB = ('AAAAAA', 'AABABB', 'AABBAB', 'AABBBA', 'ABAABB',
               'ABBAAB', 'ABBBAA', 'ABABAB', 'ABABBA', 'ABBABA')

    code_full = '101'
    code_of_digit = ''

    # комбинация для цифр 2-7
    code_AB = list_AB[int(acode[0])]

    for pos in range(1, 13):
        # текущуя цифра
        digit = int(acode[pos])

        # выбор списка кодирования
        if pos in range(1, 7):
            ch_of_code = code_AB[pos-1]
        else:
            ch_of_code = 'C'

        # дополнение до полного кода
        if ch_of_code == 'A':
            code_of_digit = list_A[digit]
        elif ch_of_code == 'B':
            code_of_digit = list_B[digit]
        elif ch_of_code == 'C':
            code_of_digit = list_C[digit]

        if pos == 7:
            code_full += '01010'

        code_full += code_of_digit
    # end of for

    return code_full + '101'


###############################################


text_code = coding('2123456050011')

print(text_code)

print(check_digit('2123456050011'))

root = Tk()

canvas_width = 150
canvas_height = 50
cnv = Canvas(root, width=canvas_width, height=canvas_height)
cnv.pack()

cnv.create_rectangle(1, 1, canvas_width, canvas_height, )

image1 = Image.new("RGB", (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image1)


y1 = int(canvas_height / 4)
y2 = y1 + 30
x = 20

end_of_rng=len(text_code)

for i in range(0, end_of_rng):
    # print(i)
    if text_code[i] == '1':
        # cnv.create_rectangle(x1, y, x1, y + 30, fill='black')
        cnv.create_line(x, y1, x, y2, fill='black')
        draw.line([x, y1, x, y2,], 'black')
    x += 1
# for #

cnv.update()

image1.save('my_barcode.jpg')

# cnv.postscript(file='barcode.ps', colormode='mono')
# os.system('convert ' + 'barcode.ps' + ' ' + 'barcode.png')
os.system('lpr my_barcode.jpg')

mainloop()
