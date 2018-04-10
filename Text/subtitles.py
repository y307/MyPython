#!/usr/bin/env python3
# -*- coding: utf-8 -*-


fin = open('in.srt')
fout = open('out.srt', 'wt')
buf_lines = ['', '', '', '']
time_line = ''
num = 0


def shift_lines():
    buf_lines[0] = buf_lines[2]
    buf_lines[1] = buf_lines[3]
    buf_lines[2] = ''
    buf_lines[3] = ''


def format_time(astr=''):
    time_list = astr.split(':')
    time_str = time_list[0].zfill(2) + ':' + time_list[1].zfill(2)
    if len(time_list) == 2:
        time_str = '00:' + time_str
    return time_str


for line in fin:
    num += 1
    ind = num % 2
    buf_lines[3 - ind] = line.replace('\n', '')
    if ind % 2 == 0:
        if buf_lines[0] != '':
            # for i in range(4):
            #    buf_lines[i]=buf_lines[i].replace('\n', '')
            time_start = format_time(buf_lines[1])
            time_stop = format_time(buf_lines[3])
            fout.write(str(num) + '\n')
            fout.write(time_start + ' --> ' + time_stop + '\n')
            fout.write(buf_lines[0] + '\n\n')
        ########################################
        shift_lines()

    else:
        pass
