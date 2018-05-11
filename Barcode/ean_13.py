#!/usr/bin/python3
# -*- coding: utf-8 -*-

# EAN-13


def check_digit(acode):
    pos = 11
    factor = 3
    summ = 0

    while pos >= 0:
        # четные позиции умножаются на 3
        summ += int(acode[pos]) * factor
        # смена множителя на 1 или 3 при каждой итерации
        factor = 4 - factor
        # позиция следующей цифры
        pos -= 1

    res = summ % 10
    if res != 0:
        res = 10 - res

    return res  # def check_digit


######################################################################


def coding(acode):
    list_A = ('0001101', '0011001', '0010011', '0111101', '0100011',
              '0110001', '0101111', '0111011', '0110111', '0001011')
    list_B = ('0100111', '0110011', '0011011', '0100001', '0011101',
              '0111001', '0000101', '0010001', '0001001', '0010111')
    list_C = ('1110010', '1100110', '1101100', '1000010', '1011100',
              '1001110', '1010000', '1000100', '1001000', '1110100')
    list_AB = ('AAAAAA', 'AABABB', 'AABBAB', 'AABBBA', 'ABAABB',
               'ABBAAB', 'ABBBAA', 'ABABAB', 'ABABBA', 'ABBABA')

    code_full = '101'
    code_of_digit = ''

    # комбинация для цифр 2-7
    code_AB = list_AB[int(acode[0])]

    for pos in range(1, 13):
        # текущуя цифра
        digit = int(acode[pos])

        # выбор списка кодирования
        if pos in range(1, 7):
            ch_of_code = code_AB[pos - 1]
        else:
            ch_of_code = 'C'

        # дополнение до полного кода
        if ch_of_code == 'A':
            code_of_digit = list_A[digit]
        elif ch_of_code == 'B':
            code_of_digit = list_B[digit]
        elif ch_of_code == 'C':
            code_of_digit = list_C[digit]

        if pos == 7:
            code_full += '01010'

        code_full += code_of_digit
    # end of for

    return code_full + '101'  # def coding


######################################################################
