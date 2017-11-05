#!/usr/bin/python3.5

from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path


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
    file_name = entry_path.get()
    folder = os.path.split(file_name)
    with open(file_name, 'r') as fin:
        for line in fin.readline():
            if line == 'BEGIN:VCARD':
                new_path = os.path.join(folder, 'tmp.vcf')
                with open(new_path, 'w') as fout:
                    fout.write(line)



button_do = Button(root, text='Выполнить', command=do_file)
button_do.place(x=10, y=65)

root.mainloop()