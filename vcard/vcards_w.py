#!/usr/bin/python3.5

from tkinter import *
from tkinter.filedialog import askopenfilename


root = Tk()
root.title('VCards')
root.resizable(False, False)
root.geometry('300x100')


def choice_file():
    fin = askopenfilename()
    entry_path.insert(0, fin)


button_path = Button(root, text='Путь к vcf-файлу...', command=choice_file)
button_path.place(x=10, y=10)

entry_path = Entry()
entry_path.place(x=10, y=37, width=280)


def do_file():
    folder =
    with open(entry_path.get(), 'r') as fin:
        for line in fin.readline():
            if line == 'BEGIN:VCARD':
                open('')



button_do = Button(root, text='Выполнить', command=do_file)
button_do.place(x=10, y=65)

root.mainloop()