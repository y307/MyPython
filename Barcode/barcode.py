#!/usr/bin/python3
# -*- coding: utf-8 -*-

# barcode EAN-13

from tkinter import *
from tkinter.ttk import *
from Barcode.ean_13 import check_digit, coding
# from PIL import Image, ImageDraw

#####################################################

root = Tk()
root.title('Печать талонов')
root.geometry('330x200')

frame1=Frame(root)
frame1.grid(row=0, column=0, columnspan=3)

lbl_sheets = Label(frame1, text=' Листов:')
lbl_sheets.pack()
#lbl_sheets.grid(column=0, row=0)
txt_sheets = Entry(frame1, width=3)
txt_sheets.pack()
#txt_sheets.grid(column=1, row=0)

'''
lbl_start = Label(root, text='   Начальн.№:')
lbl_start.grid(column=2, row=0)
txt_start = Entry(root, width=7)
txt_start.grid(column=3, row=0)
btn_start_clear = Button(root, text='X', width=1)
btn_start_clear.grid(column=4, row=0)

lbl_ser = Label(root, text='  Серия:')
lbl_ser.grid(column=5, row=0)
txt_ser = Entry(root, width=1)
txt_ser.grid(column=6, row=0)
'''

mainloop()

'''
text_code = coding('2123456050011')

print(text_code)

print(check_digit('2123456050011'))

canvas_width = 300
canvas_height = 200
cnv = Canvas(root, width=canvas_width, height=canvas_height)
cnv.pack()
cnv.create_rectangle(1, 1, canvas_width, canvas_height, outline='red')

combo = Combobox(root)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(5)  # set the selected item
combo.pack()

image1 = Image.new("RGB", (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image1)

y1 = int(canvas_height / 4)
y2 = y1 + 30
x = 20

end_of_rng = len(text_code)
for i in range(0, end_of_rng):
    # print(i)
    if text_code[i] == '1':
        # cnv.create_rectangle(x1, y, x1, y + 30, fill='black')
        cnv.create_line(x, y1, x, y2, fill='black')
        draw.line([x, y1, x, y2, ], 'black')
    x += 1
# for #

cnv.update()

image1.save('my_barcode.jpg')

cnv.postscript(file='tmp.ps', colormode='color')

# os.system('convert ' + 'barcode.ps' + ' ' + 'barcode.png')
# os.system('lpr my_barcode.jpg')

# p = os.popen('lpr', 'w')
# inf=open('barcode.ps')
# for line in inf:
# p.write(line)
# for #

# p.close()
# inf.close()
'''
