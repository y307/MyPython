#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# barcode EAN-13


def check_digit(aCode):
    pos = 11
    factor = 3
    summ = 0

    while pos >= 0:
        # четные позиции умножаются на 3
        summ += int(aCode[pos:pos+1]) * factor
        # смена множителя на 1 или 3 при каждой итерации
        factor = 4 - factor
        # позиция следующей цифры
        pos -= 1

    res = summ % 10
    if res != 0:
        res = 10 - res

    return res

def coding(aCode):



print(check_digit('5070600050015'))
