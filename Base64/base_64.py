#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import base64
import sys

# разбор аргументов коммандной строки
#if __name__=="__main__":
#    if len(sys.argv) != 3:
#        print("Введите команду в формате: base_64.py -[e|d] <путь_к_файлу>")
#        sys.exit(1)
#    else:
        #mode = sys.argv[1]
        #fin_name = sys.argv[2]
mode = "-d"
fin_name = "in.txt"

fin = open(fin_name)
fout = open("out.txt", "wb")

if mode == '-e':
    # read text from file
    encodeText = fin.read()
    # convert text to bytes
    byte_encode=encodeText.encode()  # default parameter 'utf8'
    # encode text
    encodedText = base64.b64encode(byte_encode)
    print(encodedText)
    # write encoded text to file
    fout.write(encodedText)
elif mode == '-d':
    decodeText = fin.read()
    decodeText = decodeText.replace('\n', '')
    # decode encoded text
    decodedText = base64.b64decode(decodeText)
    ttt = str(decodedText, '')
    print(ttt)
    # write decoded text to file
    # fout.write(str(decodedText).encode('latin1'))

# close opened files
fout.close()
fin.close()


# Режим открытия файла
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись
