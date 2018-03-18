#!/usr/bin/python3
# coding: utf8

import sys

# проверка на самостоятельность запуска модуля
if __name__ != '__main__':
    sys.exit(1)

debug = True  # отладка в процессе разработки кода

# проверка колчества аргументов программы
if not debug and len(sys.argv) != 5:
    print('Недостаточное количество аргументов!')
    sys.exit(1)

if not debug:
    # обработка аргументов коммандной строки
    pass  # пока не будем обрабатывать
else:   # режим отладки
    name_file1 = 'file1.html'
    name_file2 = 'file2.html'
    name_file_res = 'fileres.html'

# fileRes = open(nameFileRes, 'w')


def get_data_lines(a_name):
    file = open(a_name)
    lines = []
    word = '<body'
    flag = False

    for line in file:
        if not flag and word not in line:
            continue
        else:
            if word in line:
                if word[1] != '/':
                    word = '</body'
                flag = not flag
                continue
            lines.append(line)

    file.close()
    return lines


lines1 = get_data_lines(name_file1)

for line in lines1:
    print(line)

lines2 = get_data_lines(name_file2)

for line in lines2:
    print(line)
