#!/usr/bin/env python
# -*- coding: utf-8 -*-


fin = open('test.txt', "r")
fout = open('new.txt', "w")
n = 0

for line in fin:
    # if line.strip(" ").isnumeric():
    # fout.write(line)
    line = line.replace('_', '')
    line = line.replace("  ", " ")
    # if line[:4] == "   -":
    #    line = line.replace("   -", "     -", 1)
    # elif line[:1] == "-":
    #    line = line.replace("-", "     -", 1)
    if line.strip() == "":
        n = n+1
        if n == 1:
            fout.write(line)
        else:
            continue
    elif line[-2:-1] in [".", ":", "!", "?"]:
        fout.write(line)
        if n != 0:
            n = 0
    else:
        fout.write(line.replace('\n', " "))
        if n != 0:
            n = 0

fin.close()
fout.close()
