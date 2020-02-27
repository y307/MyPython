#!/usr/bin/env python3

import base64
import sys


# mode = "-d"
# fin_name = "in.txt"
# fin_name = ''
# mode = ''

def work_with_file():
    fin = open(fin_name)
    # fout_list = fin_name.split('.')

    if mode == '-e':
        fout_name = fin_name.replace('.', '.e.')
        fout = open(fout_name, "wb")
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
        fout_name = fin_name.replace('.', '.d.')
        decodeText = fin.read()
        decodeText = decodeText.replace('\n', '')
        # decode encoded text
        decodedText = base64.b64decode(decodeText)
        fout = open(fout_name, 'wb')
        #ttt = str(decodedText, '')
        #print(ttt)
        # write decoded text to file
        fout.write(str(decodedText).encode('latin1'))

    # close opened files

    fin.close()
    fout.close()



# разбор аргументов коммандной строки
if __name__ == "__main__":
   if len(sys.argv) != 3:
       print("Введите команду в формате: base_64.py -[e|d] <путь_к_файлу>")
       sys.exit(1)
   else:
       mode = sys.argv[1]
       fin_name = sys.argv[2]



# Режим открытия файла
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись
