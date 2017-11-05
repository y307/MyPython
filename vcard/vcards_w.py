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


def


def get_new_filename(a_line):
    list_name = a_line.split(';')
    for str_buf in list_name:
        if str_buf==''
            continue
        list_ch = str_buf.split('=')
    # todo: доделать
    return ''

def do_file():
    file_name = entry_path.get()
    folder = os.path.split(file_name)
    num = 1
    with open(file_name, 'r') as fin:
        for line in fin.readline():
            if line == 'BEGIN:VCARD':  # начало блока
                new_path = os.path.join(folder, 't'+str(num)+'.vcf')
                new_name = ''
                with open(new_path, 'w') as fout:
                    fout.write(line)
                    for line_next in fin.readline():
                        # list_buf = line_next.split(line_next, ';')
                        if line_next[0:2] == 'N;':  # строка с именем
                            res = line_next.find(':=', 0)
                            if res > -1:
                                new_name = get_new_filename(line_next[1:])
                        elif line_next == 'END:VCARD':
                            fout.write(line_next)
                            if new_name == '':
                                num += 1
                            else:
                                pass  # todo: переименовать файла
                            break
                        else:
                            pass  # todo: запись в файл


button_do = Button(root, text='Выполнить', command=do_file)
button_do.place(x=10, y=65)

root.mainloop()