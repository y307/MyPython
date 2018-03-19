#!/usr/bin/python3
# coding: utf8

import sys
import difflib

# проверка на самостоятельность запуска модуля
from builtins import print

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


# функция выделения тела нтмл файла
def get_data_lines(a_name):
    fin = open(a_name)  # открыть файл для чтения
    lines = []  # пустой список
    word = '<body'  # начало тела нтмл файла
    flag = False  # флаг записи строк

    for line in fin:
        if not flag and word not in line:
            continue
        else:
            if word in line:
                if word[1] != '/':
                    word = '</body'  # конец тела нтмл файла
                flag = not flag
                continue
            lines.append(line)

    fin.close()  # закрыть файл
    return lines


lines1 = get_data_lines(name_file1)  # список строк 1-го файла

'''for line in lines1:
    print(line)
'''

lines2 = get_data_lines(name_file2)  # список строк 2-го файла

'''for line in lines2:
    print(line)
'''

diff = difflib.ndiff(lines1, lines2)  # разница между файлами (весь diff в массиве памяти)
print(''.join(diff))

diff = difflib.HtmlDiff(tabsize=4).make_file(lines1, lines2)  # разница между файлами в виде нтмл
fout = open(name_file_res, 'w')
fout.writelines(diff)  # запись нтмл в файл
fout.close()
# print(''.join(diff))
