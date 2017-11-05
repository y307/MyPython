# !/usr/bin/python3
# coding: utf8


import os


'''
hexDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15}
'''

testStr = '0123456789ABCDEF'


def new_file_name(aname):
    with open(aname, 'r') as fin:
        for line in fin.readlines():
            # res = line.find('QUOTED-PRINTABLE:', 0)
            if line[0:2] == 'N;':
                res = line.find(':=')
                if res > -1:
                    name = ''
                    # decode QUOTED-PRINTABLE
                    list_buf = line[(res+1):].split('=')
                    for ch in list_buf:
                        if ch == '':
                            continue
                        else:
                            name += chr(16*testStr.find(ch[0])+testStr.find(ch[1]))
                    # перекодировка
                    name = name.encode('latin1').decode('utf8')
                    return name
        # for =======
        return ''
# new_file_name =======


files = os.listdir('.')
for file in files:
    if '.' == file[0]:
        continue
    if file.endswith('.vcf'):
        new_name = new_file_name(file)
        pos = new_name.find(',')
        if pos > 0:
            new_name = new_name[:pos]
        pos = new_name.find(' ')
        if pos > 0:
            new_name = new_name[:pos]
        print(new_name)
