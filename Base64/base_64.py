#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import base64
import sys

# разбор аргументов коммандной строки
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Введите команду в формате: base_64.py <путь_к_файлу>")
        sys.exit(1)
    else:
        fin_name = sys.argv[1]

fin = open(fin_name)
# read text from file
encodeText = fin.read()
# convert text to bytes
byte_encode=encodeText.encode()  # default parameter 'utf8'
encodedText = base64.b64encode(byte_encode)  # encode text
print(encodedText)

decodedText = base64.b64decode(encodedText)  # decode encoded text
print(decodedText)
fout = open("out.txt", "wb")
fout.write(decodedText)  # write decoded text to file
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
