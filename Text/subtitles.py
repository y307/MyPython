#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

fin = open('in.srt')
fout = open('out.srt', 'wt')
buf_lines = ['', '', '', '']
time_line = ''
num = 0
num_k = 0


def shift_lines():
    buf_lines[0] = buf_lines[2]
    buf_lines[1] = buf_lines[3]
    buf_lines[2] = ''
    buf_lines[3] = ''


def time2sec(astr=''):
    time_list = astr.split(':')
    l = len(time_list)
    if l == 2:
        return int(time_list[0]) * 60 + int(time_list[1])
    elif l == 3:
        return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])


def sec2time_str(asec):
    hh = int(asec / 3600)
    mm = int(asec % 3600 / 60)
    ss = asec % 3600 % 60
    return '{0:02d}:{1:02d}:{2:02.3f}'.format(hh, mm, ss)


for line in fin:
    num += 1
    ind = num % 2
    buf_lines[3 - ind] = line.replace('\n', '')
    if ind % 2 == 0:
        if buf_lines[0] != '':
            # for i in range(4):
            #    buf_lines[i]=buf_lines[i].replace('\n', '')
            time_start = time2sec(buf_lines[1])
            time_stop = time2sec(buf_lines[3])
            time_diff = time_stop - time_start
            if time_diff > 60:
                time_stop = time_start + 60
            else:
                time_stop -= 0.5

            num_k += 1
            fout.write('{0:d}\n{1:s} --> {2:s}\n{3:s}\n\n'.format(num_k,
                                                                  sec2time_str(time_start),
                                                                  sec2time_str(time_stop),
                                                                  buf_lines[0]))
        #############################################################################
        shift_lines()

    else:
        pass
