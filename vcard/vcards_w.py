#!/usr/bin/python3.5
from tkinter import *
from tkinter.filedialog import askopenfilename
import os.path
from os import rename


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


def get_new_filename(a_line):
    # decode QUOTED-PRINTABLE
    res = ''
    str_ch = '0123456789ABCDEF'
    list_name = a_line.split(';')
    for str_buf in list_name:
        if str_buf == '':
            continue
        list_ch = str_buf.split('=')
        for ch in list_ch:
            if ch=='':
                continue
            res += 16*str_ch.find(ch[0])+str_ch.find(ch[1])
            res = res.encode('latin1').decode('utf8')
    return res
# get_new_filename


def do_file():
    file_name = entry_path.get()
    folder = os.path.split(file_name)
    num = 1
    with open(file_name, 'r') as fin:
        for line in fin.readlines():
            # print(line)
            if line == 'BEGIN:VCARD\n':  # начало блока
                new_path = os.path.join(str(folder), 't'+str(num)+'.vcf')
                new_name = ''
                fout = open(new_path, 'w')
                fout.write(line)
                for line_next in fin.readline():
                    # list_buf = line_next.split(line_next, ';')
                    if line_next[0:2] == 'N;':  # строка с именем
                        res = line_next.find(':=', 0)
                        if res > -1:
                            new_name = get_new_filename(line_next[1:])
                    else:
                        fout.write(line_next)
                        if line_next == 'END:VCARD':
                            fout.close()
                            break
                # for
                if new_name == '':
                    num += 1
                else:
                    rename(new_path, os.path.join(folder, new_name+'.vcf'))
# do_file


button_do = Button(root, text='Выполнить', command=do_file)
button_do.place(x=10, y=65)

root.mainloop()