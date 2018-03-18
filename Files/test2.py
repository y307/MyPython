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
else: # режим отладки
    nameFile1 = 'file1.html'

# открываем файлы для сранения в ркжиме чтения
file1 = open(nameFile1)
lines1 = []
word = '<body'
flag = False

for line in file1:
    if not flag and word not in line:
        continue
    else:
        if word in line:
            if word[1] != '/':
                word = '</body'
            flag = not flag
            continue
        lines1.append(line)
        
for line in lines1:
    print(line)

file1.close()
