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
    str_ext = '.vcf'
    file_name = entry_path.get()
    list_paths = os.path.split(file_name)
    num = 1
    with open(file_name, 'r') as f_in:
        for line in f_in.readlines():
            # print(line)
            if line == 'BEGIN:VCARD\n':  # начало блока
                t_name = 't'+str(num)+str_ext
                new_path = os.path.join(list_paths[0], t_name)
                new_name = ''
                f_out = open(new_path, 'w')
                f_out.write(line)
                for line_next in f_in.readline():
                    # list_buf = line_next.split(line_next, ';')
                    if line_next[0:2] == 'N;':  # строка с именем
                        res = line_next.find(':=', 0)
                        if res > -1:
                            new_name = get_new_filename(line_next[1:])
                    else:
                        f_out.write(line_next)
                        if line_next == 'END:VCARD':
                            f_out.close()
                            break
                # for
                if new_name == '':
                    num += 1
                else:
                    rename(new_path, os.path.join(list_paths[0], new_name+str_ext))
# do_file


button_do = Button(root, text='Выполнить', command=do_file)
button_do.place(x=10, y=65)

root.mainloop()